# Documentation

## 1. Setup
Creation of virtual environments:
```
  virtualenv [dir] -p python3.7
  source [dir]/bin/activate
```

Install requirements:
```
  pip install pip install -r requirements.txt
```

Sync your database for the first time:
```
  python manage.py makemigrations
  python manage.py migrate
```

Create an initial user:
```
  python manage.py createsuperuser
```

Run test server on localhost and port 8000:
```
  python manage.py runserver 0:8000
```



## 2. Configurations

In /auth_api/settings.py, to turn on DEBUG mode
```
DEBUG = True
```

To comment the following to enable browsable api
```
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}
```

To change database, default is sqlite3
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

## 3. API usages

To run the test, runserver on 0:8000. Then go to test folder and run in terminal:
```
sudo chmod 777 ./basic_test.sh
./basic_test.sh http://127.0.0.1:8000 
```

To view root:
```
curl [domain]/api/
```

To view list of all houses:
```
curl [domain]/api/houses/
```

To search by zip code or address:
```
curl [domain]/api/houses/?address=[address]&zipcode=[zipcode]
```

To get all post of a user:
```
curl [domain]/api/houses/?username=[username]
```

To get info of a certain house:
```
curl [domain]/api/houses/[pk]
```


To register as a user:
```
curl -X POST [domain]/api/users/ -d "username=[un]&password=[pw]"
```

To login, add the following in curl command line:
```
--user [un]:[pw]
```

To view information after login:
```
curl --user [un]:[pw] [domain]/api/users/
```

To post new listings of houses to sell (status is OM ('on market') by default):
```
curl --user [un]:[pw] -X POST [domain]/api/houses/ -d "name=[n]&address=[ad]&zipcode=[zp]&description=[des]"
```

To change house status (primekey is required) from on market to pending (PD) or sold (SD):
```
curl --user [un]:[pw] -X PUT [domain]/api/houses/[pk] -d "status=PD&name=[n]&address=[ad]&zipcode=[zp]&description=[des]"
```
