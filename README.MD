-install python and pip
(recommend latest versions of everything, python 2 not okay)
-install django

Run these commands to set everything up:
# run setup for users/admin/auth
python manage.py migrate

# run the migrations from 'mines' app
python manage.py makemigrations mines

# create admin user
python manage.py createsuperuser

messing around in console:
python manage.py shell

# for john to run dev
python3.6 manage.py runserver

NOTE: if we move from SQLite to something else, delete migrations in mines/migrations
TODO:
- run security checks on prod server with `python3 manage.py check --deploy`
- setup caching from here https://docs.djangoproject.com/en/2.0/ref/settings/
- https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

on prod:
1. go inside source code dir
2. `source theminesenv/bin/activate`
3. `./manage.py runserver 0.0.0.0:8008` <-- no, this is only for dev environment
