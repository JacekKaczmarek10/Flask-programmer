# flask-programmer
Flask programmer task


###############################################################################################
To run this application simply run in terminal in folder with program location:
python app.py


##########################################################################
But first you need to import some things(in windows)
In terminal:
(Do if virtualenv is not activated):

.\env\Scripts\activate.bat

python -m pip install requests  

pip3 install Flask

pip3 install Flask-SQLAlchemy

pip3 install Flask-Migrate

pip3 install pillow

then finally:

python app.py
#######################################################################
Seeding Database

to create database type in terminal:
flask db_create

to seed data base with 3 example assistants:
flask db_seed

to delete all data:
flask db_drop

