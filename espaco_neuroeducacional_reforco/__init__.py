import os
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_wtf import CSRFProtect

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contato.db'
database = SQLAlchemy(app)

bootstrap = Bootstrap5(app)

from flask_bcrypt import Bcrypt
from espaco_neuroeducacional_reforco import routes

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') # resolver essa parte do código
csrf = CSRFProtect(app)

bcrypt = Bcrypt(app)
