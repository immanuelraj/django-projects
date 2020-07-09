### Project Setup for Mac
* Install python
    ```sh
    brew install python3
    ```
* Install postgres
    ```sh
    brew install postgres
    brew install postgresql
    ```
* Start postgres
    ```sh
    brew service start postgres
    ```
* Create db
    ```sh
    createdb masterdb
    ```
* Clone project
    ```sh
    git clone https://github.com/immanuelraj/django-project.git
    cd django-project/
    ```
* Create virtualenv
    ```sh
    brew install mkvirtualenv
    mkvirtualenv --python=/usr/local/bin/python3 django-project
    workon django-project
    ```
* Install packages
    ```sh
    pip install -r requirements.txt
    ```
* To run the project
    ```sh
    cd project
    python manage.py migrate
    python manage.py collectstatic
    python manage.py createsuperuser
    python manage.py runserver
    ```
    
### Project Setup for Ubuntu
* Install Python
 ```sh
 Sudo apt install python3.7
 ```

* Install postgres
```sh
sudo apt install postgresql postgresql-contrib
sudo su postgres
createdb masterdb
 ```
* Clone project
```sh
git clone https://github.com/immanuelraj/django-project.git
cd django-project/
 ```
* Create virtualenv
```sh
sudo apt-get install python-pip
sudo pip install virtualenv
mkdir ~/.virtualenvs
sudo pip install virtualenvwrapper
export WORKON_HOME=~/.virtualenvs
. /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv django-project
workon django-project
pip install -r requirements.txt
 ```
* To run the project
```sh
cd project
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
python manage.py runserver
 ```


### Docker Setup by docker-compose

* Download and Install docker application on mac

* Create docker-compose.yml file and Add the Instruction

* To run docker compose
    ```sh
    docker-compose up -d
    ```
* To stop docker compose
    ```sh
    docker-compose down
    ```
* connecting to django shell
    ```sh
    docker-compose exec web bash
    python manage.py shell
    ```
* connecting to postgres
    ```sh
    docker-compose exec db bash
    psql -U admin masterdb
    ```

### Docker Image and container

* Create Dockerfile and Add the Instruction
* Create a docker image
    ```sh
    docker build -t myimage:1 .
    ```
* Create a docker container from image
    ```sh
    docker images
    docker run imageid
    ```
* To clean up space used by docker
    ```sh
    docker system prune -a
    docker volumes prune
    ```

### Heroku Setup

* Install Heroku
    ```sh
    brew install heroku/brew/heroku
    ```
* To Login to Heroku
    ```sh
    heroku login
    ```
* Create heroku App
    ```sh
    heroku create django-project-app
    ```
* Install django-heroku package and add it in settings
* Add Procfile under root directory
* Add domain to allowed_host
* To push to Heroku
    ```sh
    git push heroku master
    ```
* Basic Setup
    ```sh
    heroku run python manage.py migrate
    heroku run python manage.py createsuperuser
    ```
* Add config
    ```sh
    heroku config:set SECRET_KEY='key'
    ```

### Features

* Login URL
    ```sh
    https://immanuelraj.herokuapp.com/accounts/login/

* SignUp URL
    ```sh
    https://immanuelraj.herokuapp.com/accounts/signup/
    ```

* Portfolio
    ```sh
    https://immanuelraj.herokuapp.com/
    ```

* Create Dummy data
    ```sh
    python manage.py create_dummy_data
    ```
* User Activity API
    ```sh
    https://immanuelraj.herokuapp.com/activity/user-activity/
    https://immanuelraj.herokuapp.com/activity/user-activity/?search=vwyfj9k1gr
    https://immanuelraj.herokuapp.com/activity/user-activity/?page=2
    ```
* To add hotel
    ```sh
    cd ../scripts
    python add_hotel.py
    or
    https://immanuelraj.herokuapp.com/admin/hotel/hotel/add/
    ```
* To add room
    ```sh
    python add_room.py
    or
    https://immanuelraj.herokuapp.com/dmin/hotel/room/add/
    ```
* To view rooms
    ```sh
    python room_list.py
    or
    https://immanuelraj.herokuapp.com/hotel/room-list/
    ```
* To view rooms by budget
    ```sh
    python price_wise_room_list.py
    or
    https://immanuelraj.herokuapp.com/hotel/room-list/?budget=50
    ```
