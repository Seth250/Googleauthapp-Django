## Googleauthapp-Django
Simple Google Authentication app in Django with the social auth app library 

## Introduction
This is a repository that shows a simple way to setup google authentication in Django using the social-auth-app-django library

## Requirements
* Python3
* Pipenv
* Django
* Social auth app Django

## Running the Application
* Make sure all requirements are installed
* Create a Virtual Environment in the shell, if there is not an existing one
* Run ```[workon yourvirtualenv]``` to enable the Virtual Environment
* Make a directory for your Django files ```[mkdir yourdirectoryname]```
* Change the path to that directory ```[cd yourdirectoryname]```
* Create a new Django Project if there is not an existing one ```[django-admin startproject myprojectname]```
* Change the path to the project directory ```[cd myprojectname]```
* Make migration ```[python manage.py migrate]``` 
* Run the Server ```[python manage.py runserver]```
* Open your Browser and run http://localhost:8000 or http://127.0.0.1:8000 

# NOTE:
* Please Make Sure that ```SOCIAL_AUTH_GOOGLE_OAUTH2_KEY``` and ```SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET``` in ```[settings.py]``` are both filled with the right keys, they are left blank by default for Security reasons
* You can get your unique Keys from https://console.developers.google.com
