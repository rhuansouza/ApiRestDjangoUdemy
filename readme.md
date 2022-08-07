python.exe -m pip install --upgrade pip
python -m venv venv
python manage.py createsuperuser
python manage.py runserver
python manage.py migrate
python manage.py makemigrations
pip install djangorestframework
pip install django-filter