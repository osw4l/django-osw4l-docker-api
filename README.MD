

# Django Osw4l Docker
It is a beautiful Django image simple to configure, run and deploy, it was made with a lot of love and dedication for all human beings who love simple things.

this project contains the next libraries

 - Django
 - uWSGI
 - asgiref
 - django-celery-beat
 - django-celery-results
 - django-cors-headers
 - django-environ
 - django-extensions
 - django-rest-swagger
 - djangorestframework
 - djangorestframework-gis
 - django-leaflet
 - django-map-widgets
 - djangorestframework-simplejwt
 - psycopg2
 - postgis
 - redis
 - Pillow
 - django-storages
 - boto
 - botocore
 - s3transfer
 
and more pretty stuff like
 - Docker compose
 - Django Channels
 - Postgis 
 - Geo Django
 - Leaflet and Google Maps
 - Celery Worker and Celery Beat
 - Nginx with django static files support
 - Static files working fine !
 - AWS S3 Storage
 - Natural structure, **like you weren't using docker**
 - Production deploy steps [click here](https://gist.github.com/osw4l/cbfbfb3f7a7f42ab31fa5083b358f316)

Simple and beautiful structure

 ![enter image description here](https://i.imgur.com/rUXVwk6.png)

to run  the image follow the next instructions, just for local environment

## Create Environment file

    cp .env_template .env

## build image

    docker-compose build

## up image

    docker-compose up -d 

## create migrations

    docker-compose exec backend python3 manage.py migrate

## restart celery beat

    docker-compose restart beat

## create superuser

    docker-compose exec backend python3 manage.py createsuperuser

## collect statics

    docker-compose exec backend python3 manage.py collectstatic


## Pycharm Support
first, we need to setup the common stuff to active the autocomplete adding the Django Support choosing the manage.py and settings.py files location.

![enter image description here](https://i.imgur.com/yxaLtUc.png)

now we need add the python interpreter what live inside the docker container to the project

Go to preferences and to click in Interpreter then in Project Interpreter and press add

![enter image description here](https://i.imgur.com/DwKsssx.png)

now, do click in Docker, select the image what contains the project name, then write python3 and press ok

![enter image description here](https://i.imgur.com/pI86DZb.png)

press apply and ok, done!.

![enter image description here](https://i.imgur.com/lmpULSQ.png)

now we have configured the interpreter what lives inside our Docker Container in our project

Please, DON'T UPDATE THE DEPENDENCIES ! **unless necessary**

if you wanna deploy this project in production, [go to here](https://gist.github.com/osw4l/cbfbfb3f7a7f42ab31fa5083b358f316)


**Thanks for using my project, if you need something else, feel you free to contact me**
**me@osw4l.com**
