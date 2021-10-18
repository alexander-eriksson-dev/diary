# diary
My first Github repo. A simple diary built using Python with Django.

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
Create file '.env' in same directory as settings.py containing (code generated from eg djecrety.ir):
```
SECRET_KEY='PASTE_HERE'
```
Create a database and add a superuser:

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