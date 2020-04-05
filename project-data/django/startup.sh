cd /usr/src/app/django/webapps

#/manage.py collectstatic --noinput
./manage.py makemigrations
./manage.py migrate

#./manage.py runserver 0.0.0.0:8088

cd /usr/src/app/django
uwsgi --ini   uwsgi.ini 
