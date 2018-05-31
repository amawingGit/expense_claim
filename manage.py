from IPython import embed
from sqlalchemy import create_engine
import click
from app.environment import create_environment, db
from os import environ
from app.models import Base

@click.group()
@click.option(
    '--db_url',
    default=environ['DB_URL'],
    help='Database connection string.'
)
def cli(db_url):
    #logger.info('Using DB_URL: {}'.format(colored.red(db_url)))
    engine = create_engine(db_url, echo=True)
    db.init(engine=engine)
    create_environment()

@cli.command(help='Create all the tables in the schema.')
def create_all():    
    db.create_all(Base)


@cli.command(help='Drop all the tables in the schema.')
def drop_all():    
    db.drop_all(Base)    

@cli.command(help='Run shell.')
def shell():   
    session = db.Session()
    #mixer = FixedMixer(session=session, commit=True) # NOQA

    embed(banner1='Welcome to the Pricing Service!')


if __name__ == '__main__':
    cli()
