# Hello world in Django  #
### the project has: ###
- button what dynamically create a field as input using js;
- button what to remove added fields;
- button what to send data to wsgi application;
- the server receives data and writes it to the database using JSONField;
- displaying everything added in the database on web page.

### application launch playback steps ###
You must have installed python==3.8, git and server PostgerSQL in you system.
- git clone https://github.com/iamstanisla/hzhz0812.git
- cd hzhz0812
- python3 -m venv venv
- activate
- python3 -m pip install -r requirements.txt
- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 manage.py runserver

You will see messages about starting the server.
Open a url localhost:8000 in yout browser.
