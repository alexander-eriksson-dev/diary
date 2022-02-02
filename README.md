# journal
A simple journal built with Python. 

* Django web framework
* Bootstrap for responsive scaling/design
* Markdown for simple text editing
* Runs on Gunicorn
* PostgreSQL database

![Demo screenshot](https://i.imgur.com/5mjTFIw.png)

My first Github repo, this is for me to practice managing a project, using git, deploying to a server like Heroku and providing instructions for you to run this on your own machine. Updating as I learn.. 😁

## DEMO:
This Github repo is automatically deployed on Heroku when pushed to. You can try it out here: 

[JOURNAL APP DEMO](https://warm-scrubland-19058.herokuapp.com/)

If you dont bother registering: 
Username: demo
Password: github123

## Credit:
Based on [this tutorial from RealPython](https://realpython.com/django-diary-project-python/)

## 💨 How to run yourself:
Clone repo
```
git clone https://github.com/alexander-eriksson-dev/journal
```
Create a virtual environment and install requirements
```
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```
Migrate database and add an admin user
```
python manage.py migrate
python manage.py createsuperuser
```
Collect static files
```
python manage.py collectstatic
```
Run local server:
```
python manage.py runserver
```
👏🏼👏🏼
