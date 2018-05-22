from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

def create_app(environment='development'):
    app = Flask(__name__)     
    app.config.from_pyfile('../settings.py', silent=True)
    #db.init_app(app)
    
    @app.route('/')
    def home():
        return render_template('home.html')
    
    @app.route('/hello')
    def hello_world():
        return 'Hello, World!'

    return app    
