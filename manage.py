from IPython import embed
from sqlalchemy import create_engine, func
import click
from app.environment import create_environment, db
from app.seeds import load_seeds
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
    from app.models.user import User
    from app.models.expense_claim import ExpenseClaim
    # from app.models.expense_department import ExpenseDepartment
    # from app.models.approval import Approval

    session = db.Session()


    embed(banner1='Welcome to the Pricing Service!')

@cli.command(help='Run seeds.')
def run_seeds(): 
    load_seeds()


if __name__ == '__main__':
    cli()
