import logging
from os import environ
from sqlalchemy import create_engine


from app.classes.database_helper import DatabaseHelper  # NOQA

db = DatabaseHelper()

def create_environment(environment='development'):
    if environment == 'test':
        engine = create_engine('sqlite://')
    else:
        engine = create_engine(environ['DB_URL'])

    db.init(engine=engine)

