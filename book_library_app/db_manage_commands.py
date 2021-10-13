import json
from pathlib import Path
from book_library_app import app, db
from book_library_app.models import Author
from datetime import datetime


@app.cli.group()
def db_manage():
    """Database management command"""
    pass


@db_manage.command()
def add_data():
    """Add sample data to database"""
    try:
        authors_path = Path(__file__).parent / 'samples' / 'authors.json'
        with open(authors_path) as file:
            data_json = json.load(file)
        for item in data_json:
            item['birth_date'] = datetime.strptime(item['birth_date'], '%d-%m-%Y').date()
            4
            author = Author(**item)
            db.session.add(author)
        db.session.commit()
        print("Data has been successfully added to database")
    except Exception as exc:
        print("Unexpected error: {}".format(exc))


@db_manage.command()
def remove_data():
    """Remove all data from database"""
    try:
        db.session.execute('TRUNCATE TABLE authors')
        db.session.commit()
        print("Data has been successfully removed")
    except Exception as exc:
        print("Unexpected error: {}".format(exc))
