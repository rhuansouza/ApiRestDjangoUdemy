python.exe -m pip install --upgrade pip
python -m venv venv
python manage.py createsuperuser
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
pip install djangorestframework
pip install django-filter

python manage.py shell
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
rh = User.objects.get(id=2)
token = Token.objects.create(user=rh)
token.key
74ec6ecdae4badc8ed36af9fb153950bec99da98
