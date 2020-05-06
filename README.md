## Project Setup

### Install python
 - brew install python3
### Install postgres
 - brew install postgres
 - brew install postgresql
### Start postgres
 - brew service start postgres
### Create db
 - createdb masterdb
### Clone project
 - git clone https://github.com/immanuelraj/django-project.git
 - cd django-project/
### Create virtualenv
 - brew install mkvirtualenv
 - mkvirtualenv --python=/usr/local/bin/python3 django-project
 - workon django-project
### Install packages
 - pip install -r requirements.txt
### To run the project
 - cd project
 - python manage.py migrate
 - python manage.py collectstatic
 - python manage.py createsuperuser
 - python manage.py runserver


## Heroku Setup

### Install Heroku

- brew install heroku/brew/heroku

### To Login to Heroku

- heroku login

### Create heroku App

- heroku create django-project-app

### Install django-heroku package and add it in settings

### Add Procfile under root directory

### Add domain to allowed_host

### To push to Heroku

- git push heroku master

### Basic Setup

- heroku run python manage.py migrate
- heroku run python manage.py createsuperuser


## Features

### Create Dummy data
- python manage.py create_dummy_data

### User Activity API
- https://django-project-app.herokuapp.com/activity/user-activity/
- https://django-project-app.herokuapp.com/activity/user-activity/?search=vwyfj9k1gr
- https://django-project-app.herokuapp.com/activity/user-activity/?page=2

### To add hotel
cd ../scripts
 - python add_hotel.py
 - https://django-project-app.herokuapp.com/admin/hotel/hotel/add/
### To add room
 - python add_room.py
 - https://django-project-app.herokuapp.com/admin/hotel/room/add/
### To view rooms
 - python room_list.py
 - https://django-project-app.herokuapp.com/hotel/room-list/
### To view rooms by budget
 - python price_wise_room_list.py
 - https://django-project-app.herokuapp.com/hotel/room-list/?budget=50
