# Event App

It is a event app where APIs are used to perform CRUD operations.

## Installation Notes

To create a Virtual Environment. Simply run

```
poetry shell
```

If you haven't installed Poetry into your Local machine or Server. Please Install Poetry.
For Installing Documentations [Click Here](https://python-poetry.org/docs/#installation)

Install the Project Requirements from ``poetry.lock``.

```
poetry install
```

Set up ``.env`` file in the folder directory ``conf/settings/.env``. 
Sample ``.env`` file is in the ``.env.example`` file. Add the necessary environment variable values.

Run the entrypoint.sh file to install internal dependencies
```
./entrypoint.sh
```

To execute locally, simply run the ``manage.py`` file

```
python manage.py runserver
```

### To run using Docker

```
docker-compose build
```

```
docker-compose up -d
```

### To run the project using Docker [Local Dev only]

Set up you db creds of .env file according to docker-compose.yml.dev  
Change your .env file like this if you do not want to change the docker-compose file.

```
# Database Settings
DB_NAME=event-local-db
DB_USER=postgres
DB_PASSWORD=asdf
DB_PORT=5432
DB_HOST='db'
```

Run the following command
```
docker-compose -f docker-compose.yml.dev build
```

```
docker-compose -f docker-compose.yml.dev up -d
```

## E2E Testing

To run end-to-end test simply run the command below. This will generate code coverage report.

```
pytest --cov=EventApp
```

## API Documentation

Check the APIs in Swagger and Redoc (Only in Dev and Stage environment)

**Redoc**

```
http://127.0.0.1:8000/redoc/
```

**Swagger Doc**

```
http://127.0.0.1:8000/doc/
```

## Built With

* [Python](https://www.python.org/) - Language Used
* [Django](https://www.djangoproject.com/) - Framework Used
* [Django Rest Framework](https://www.djangoproject.com/) - Restfull Library Used
* [Psycopg](https://www.psycopg.org/docs/) - PostgreSQL Database Adapter for Python
* [Poetry](https://python-poetry.org/docs/) - Python dependency management and packaging

## GIT branching Strategies
**Gitflow** is used as a Git workflow here that will help with continuous software development and implementation of
DevOps practices.

## Folder Structure

```
EventApp/               # Root Folder
|- apps/                # Main application folder that consists of all the project apps
    |- event/           # Project app
        |- static/      # App specific static file folder
        |- templates/   # App specific templates file folder
            |- event/
        |- tests/       # App specific test suit folder
        |- utils/       # App specific utility file folder
        |- views/       # Folder contains all the views for the app
        |- admin.py
        |- apps.py
        |- models.py
        |- urls.py
|- conf/                # Base folder for all the configuarations
    |- settings
        |- .env
        |- .env.example
        |- base.py      # Base settings file
        |- development.py # Settings file for developments environment
        |- production.py # Settings file for production environment
    asgi.py
    urls.py
    wsgi.py
|- core/                # Base app
    |- constants
        |- constants.py
        |- defaults.py
    admin.py
    apps.py
    tests.py
    utils.py
    models.py
    mixins.py
    ...
|- log                  # Folder for all the logs
|- static
|- templates
|- .gitignore           # gitignore
|- Dockerfile
|- docker-compose.yml
|- manage.py            # Django's command-line utility
|- poetry.lock          # Required package file
|- pyproject.toml       # Project description file
|- README.md
```

## Design Wiki

[System Design](https://github.com/njnur/EventApp/wiki/System-Design) - Project System Design Wiki Page
