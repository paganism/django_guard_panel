# Watching storage site. It shows who and when was in the storage. Also it shows duration of presence in storage.

# How to start on linux

Recommended to use virtual environment.
Request access to the database from your bank manager. For access you need a host, port, dbname, password.
Create .env file in root directory of your project and fill it the following variables:

```
DATABASE_ENGINE = 'your db backend'
DATABASE_HOST = 'your host'
DATABASE_PORT = 'your port'
DATABASE_NAME = 'your dbname'
DATABASE_USER = 'your username'
DATABASE_PASSWORD = 'your password to db'

SECRET_KEY='your secret key'

DEBUG=FALSE
```

1. Install requirents via pip
```
$ pip3 install -r requirements.txt
```
2. Run on localhost
```
$ python3 manage.py runserver 0.0.0.0:8000
```
3. Open in prefered browser address http://0.0.0.0:8000/

# Project goals
This site is created for educational purposes only.