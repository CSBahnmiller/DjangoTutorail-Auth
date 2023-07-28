▶️Install requirements, the command for that is "pip install -r requirements.txt"
▶️Currently is setup with a Postgres Datase
▶️The Data base configs are using an alias file for it's connection, you will have to add a .env file that has this similar structure to connect to a postgress DB: 

SECRET_KEY=**Django secret key**
DB_NAME= **your Name for DB**
DB_USER=**The login for your DB**
DB_PASSWORD=**Your DB password for that login**
DB_HOST=**The address your postgres DB is at**
DB_PORT=**Default port is 5432, if not using default port change here**

** if you don't know what your SECRET_KEY is use this command from terminal in the directory with manage.py: python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'