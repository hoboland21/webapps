cd /usr/src/app/django

#webapps/manage.py collectstatic --noinput
webapps/manage.py makemigrations
webapps/manage.py migrate

webapps/manage.py runserver 0.0.0.0:8888

#uwsgi --ini   uwsgi.ini 
