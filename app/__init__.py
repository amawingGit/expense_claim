from flask import Flask, render_template
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
#from flask_migrate import Migrate
from os import environ
from app.environment import create_environment

def create_app(environment='development'):
    app = Flask(__name__)         
    create_environment(environment)

    @app.route('/')
    def home():
        return render_template('home.html')
    
    @app.route('/hello')
    def hello_world():
        return 'Hello, World!'
    
    @app.route('/users')
    def user():
        return render_template('users.html')
    
    @app.route('/expense_claims')
    def expense_claims():
        return render_template('expense_claims.html')

    return app    
