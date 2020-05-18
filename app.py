import requests
import io
import codecs
import base64

from flask import Flask, render_template, request, redirect, jsonify, send_file, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from io import BytesIO
from flask_migrate import Migrate
from shutil import copyfileobj
from PIL import Image
from urllib.request import urlopen
import shutil, sys 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)

class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.LargeBinary)

class Assistant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email_address = db.Column(db.String(80), nullable=False)
    pic_name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)


@app.route('/')
def index():
    return render_template('home.html')

def pic_2_thumbnail(image):
    im = Image.open(image)
    return im

def pic_to_bytes(im):
    imgByteArr = io.BytesIO()
    im.save(imgByteArr, format='BMP')
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr


@app.route('/assistants', methods=['GET', 'POST'])
def assistant_view():
    if request.method == 'POST':
        print(request.values)
        job_id = request.values.get('job_id')
        first_name = request.values.get('first_name')
        last_name = request.values.get('last_name')
        email_address = request.values.get('email_address')
        if request.files['inputfile'].filename != '':
            image = request.files['inputfile']
            size = 80, 80
            im = pic_2_thumbnail(image)
            im.thumbnail(size)
            x= pic_to_bytes(im)
        else:
            r = requests.get('https://randomuser.me/api')
            image_url = r.json()['results'][0]['picture']['thumbnail']
            x= requests.get(image_url).content

      


        assistant = Assistant(job_id=job_id, first_name=first_name,
        last_name=last_name, email_address=email_address,
        pic_name='hot dog', data=x)
        db.session.add(assistant)
        db.session.commit()
        
        
    # add_jobs_to_db()

    assistants_jobs = db.session.query(Assistant, Job).filter(Assistant.job_id==Job.id).all()
    pictures = [base64.b64encode(assistant.data).decode() for assistant, _ in assistants_jobs]
    assistants_jobs_pictures = [(list1[0], list1[1], picture) for list1, picture in zip(assistants_jobs, pictures)]

    return render_template('display_assistants.html', assistants_jobs_pictures=assistants_jobs_pictures)


@app.route('/assistants/create', methods=['GET'])
def add_assistant():
    jobs = Job.query.all()
    print(jobs)
    return render_template('add_assistant.html', jobs=jobs)


@app.route('/assistants/<int:id>', methods=['DELETE'])
def delete(id):
    delete_assistant = Assistant.query.get_or_404(id)

    try:
        db.session.delete(delete_assistant)
        db.session.commit()
        return jsonify({'ok': 'ok'})
    except:
        return 'there was an error deleting assistant :('


@app.route('/assistants/update/<int:id>', methods=['GET'])
def display_update(id):
        # updated_assistant = Assistant.query.get_or_404(id)

        assistant_job = db.session.query(Assistant, Job).filter((Assistant.job_id==Job.id) & (Assistant.id==id)).all()
        print(assistant_job)

        jobs = Job.query.all()
        return render_template('update_assistant.html', 
        assistant_job=assistant_job,
        jobs=jobs
        )

@app.route('/assistants/<int:id>', methods=['PUT'])
def update_assistant(id):
        updated_assistant = Assistant.query.get_or_404(id)
        data = request.json
        print(data)
        print(request)
        updated_assistant.job_id = data['job_id']
        updated_assistant.first_name = data['first_name']
        updated_assistant.last_name = data['last_name']
        updated_assistant.email_address = data['email_address']
        try:
            db.session.commit()
            return jsonify({'ok': 'ok'})
        except Exception as e:
            print(str(e))
            return 'There was an issue updating your assistant'


def add_jobs_to_db():
    r = requests.get('http://api.dataatwork.org/v1/jobs')

    if r.ok:
        jobs_data = [r for r in r.json() if 'normalized_job_title' in r]
        
        for job_data in jobs_data:
            job = Job(title=job_data['title'])
            db.session.add(job)
        
        db.session.commit()

def add_pic_to_db():
    picture_url = "https://thispersondoesnotexist.com"

    picture = request.get(picture_url, stream=True)
    picture.raw.decode_content = True
    size = 80,80
    im = pic_2_thumbnail(picture)
    im.thumbnail(size)
    x= pic_to_bytes(im)
    image = Picture(data=x)
    import base64
    data_uri = base64.b64encode(open('Graph.png', 'rb').read()).decode('utf-8')
    img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)
    print(img_tag)
    
    db.session.add(image)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)