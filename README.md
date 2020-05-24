# Client/Server Trade Application

Sample client/server FX Trading application that utilises Fixer.io as a rate provider.

Written in Python, and requireing Python >= 3.7.0.

### Overview

This project contains two architectural parts:
1. A Flask-based Web Application which provides two views: One for listing booked trades and another for placing a trade
2. A Flask-based, [Swagger 3](https://swagger.io/) documented API backend. Database storage utilises SQLite.

## Developing

### Local Setup

Ensure you have the following already available:

1. Python > 3.7.0
2. virtualenv

Then, prep your local environment as follows:

1. Setup a clean python > 3.7.0 virtual environment (hereby assumed to be in ./venv)
 ```
 virtualenv --python=python3.7 venv
 ```
2. Install dependencies via PIP 
 ```
 pip install -r requirements.txt
 ```

The components can be run outside of Gunicorn in development mode as follows:
```
CONFIG_FILE=/path/to/config.ini python /your/path/to/trading_app/api_server.py
CONFIG_FILE=/path/to/config.ini python /your/path/to/trading_app/web_client.py
```

###

## Configuration

Each application requires a configuration file, the location of which is supplied in an environment varaible `CONFIG_FILE`.

### Web Configuration

```
[app]
debug=False
port=8081
```

- app.debug: Whether to enable Flask-level debug server (not used when running under WSGI)
- app.port: Port number for Flask to listen on (not used when running under WSGI)

### API Configuration

```
[app]
debug=False
port=8080
cors_origins=http://127.0.0.1:8081

[database]
sqlite_db_path=/your/path/to/trading.db

[fixer]
access_key=YOUR_FIXER_IO_ACCESS_KEY
```

- app.debug: Whether to enable Flask-level debug server (not used when running under WSGI)
- app.port: Port number for Flask to listen on (not used when running under WSGI)
- app.cors_origins: A comma delimited list of origins permitted to make API calls
- database.sqlite_db_path: Path to SQLite database. If this doesn't exist, it will be created automatically for you
- fixer.access_key: Your access key used to call [Fixer.io](https://fixer.io)

## Deploying / Running

The simplest way to run locally is to utilise Docker Compose:

1. `docker-compose build`
2. `docker-compose up`

You will then be able to access the Web Application at http://127.0.0.1:8081