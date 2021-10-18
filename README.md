# diary
A simple diary built using Python with Django. 

My first Github repo, this is for me to practice managing a project, using git and keeping the project fairly portable for you to try this on your own machine. Updating as I learn. 

✔️ TO-DO: Improve the functionality and make it more.. stylish.

## 💨 How to run:
Clone repo
```
git clone https://github.com/alexander-eriksson-dev/diary
```
Create a virtual environment and install requirements
```
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```
Create file '.env' in same directory as settings.py containing (code generated from eg www.djecrety.ir):
```
SECRET_KEY='PASTE_HERE'
```
Migrate database and add an admin user:

```
- python manage.py migrate
- python manage.py createsuperuser
```
Run local server:
```
- python manage.py runserver
```
👏🏼👏🏼

## Credit:
Based on the project from https://realpython.com/django-diary-project-python/