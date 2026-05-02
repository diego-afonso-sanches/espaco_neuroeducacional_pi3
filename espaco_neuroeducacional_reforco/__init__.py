from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contato.db'
database = SQLAlchemy(app)

bootstrap = Bootstrap5(app)

from flask_bcrypt import Bcrypt
from espaco_neuroeducacional_reforco import routes

app.config['SECRET_KEY'] = '2e54a9fb34553a8831fdbdf814771987'

bcrypt = Bcrypt(app)
