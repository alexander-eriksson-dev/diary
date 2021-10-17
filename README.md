# diary
My first Github repo. A simple diary built using Python with Django.

✔️ TO-DO: Improve the functionality and make it more.. stylish.

## 💨 How to run:
Run by creating and activating a virtual environment and installing Django:

```
- python -m venv venv
- .venv\Scripts\activate.bat
- python -m pip install Django==3.2.1
```

Then run the database migrations and create a superuser:

```
- python manage.py migrate
- python manage.py createsuperuser
```

And run the local Django server:
```
- python manage.py runserver
```

## Credit:
Based on the project from https://realpython.com/django-diary-project-python/