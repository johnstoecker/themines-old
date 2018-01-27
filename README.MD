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

NOTE: if we move from SQLite to something else, delete migrations in mines/migrations
