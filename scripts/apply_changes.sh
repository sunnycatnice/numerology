#!/bin/zsh

#make sure to close the server before running this script
python manage.py makemigrations myapi
python manage.py migrate
python manage.py startserver

#to create a superuser -> python manage.py createsuperuser
