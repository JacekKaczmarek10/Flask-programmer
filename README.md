# flask-programmer
Flask programmer task


#########################################################################

How to run it on Windows:
In terminal

1. virtualenv env

2. .\env\Scripts\activate.bat

3. pip install -r requirements.txt

4. flask db init

5. flask db migrate -m "Initial commit"

6. flask db upgrade

7. flask db_create

8. flask db_seed

9. python app.py

Now you should be able to open url  http://127.0.0.1:5000/ in your web browser.

How to run it on linux:

1. virtualenv env

2. source env/bin/activate

3. pip install -r requirements.txt

4. python3 -m flask db init

5. python3 -m flask db migrate -m "Initial commit"

6. python3 -m flask db upgrade

7. python3 -m flask db_create

8. python3 -m flask db_seed

9. python3 app.py

Now you should be able to open url  http://127.0.0.1:5000/ in your web browser.

