from os import environ
from sqlalchemy import create_engine


from app.classes.database_helper import DatabaseHelper  # NOQA

db = DatabaseHelper()

def create_environment(environment='dev'):

    engine = create_engine(environ['DB_URL'])
    db.init(engine=engine)

