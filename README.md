# Book Library REST API
Code was implemented thanks to the Udemy course - [REST API development step by step - Python | Flask | MySQL ](https://www.udemy.com/course/rest-api-krok-po-kroku-python-flask-mysql). 
REST API for online library. It supports authors of books and books resources including authentication (JWT Token).

The documentation can be found in `documentation.html` or [here](https://documenter.getpostman.com/view/7306302/T1DjjKJd?version=latest)

## Setup

- Clone repository
- Create database and user
- Rename .env.example to `.env` and set your values
```buildoutcfg
# SQLALCHEMY_DATABASE_URI MySQL template
SQLALCHEMY_DATABASE_URI=mysql+pymysql://<db_user>:<db_password>@<db_host>/<db_name>?charset=utf8mb4
```
- Create a virtual environment
```buildoutcfg
python -m venv venv
```
- Install packages from `requirements.txt`
```buildoutcfg
pip install -r requirements.txt
```
- Migrate database
```buildoutcfg
flask db upgrade
```
- Run command
```buildoutcfg
flask run
```


**NOTE**

Import / delete example data from `book_library_app/samples`:

```buildoutcfg
# import
flask db-manage add-data

# remove
flask db-manage remove-data
```

## Tests

In order to execute tests located in `tests/` run the command:

```buildoutcfg
python -m pytest tests/
```

## Technologies / Tools

- Python 3.8.0
- Flask 1.1.2
- Alembic 1.4.2
- SQLAlchemy 1.3.16
- Pytest 5.4.3
- MySQL
- AWS
- Postman
