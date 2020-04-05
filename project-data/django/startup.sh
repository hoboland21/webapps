cd /usr/src/app/django

#/manage.py collectstatic --noinput
webapps/manage.py makemigrations
webapps/manage.py migrate

#./manage.py runserver 0.0.0.0:8088

uwsgi --ini   uwsgi.ini 
