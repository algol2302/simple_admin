import os

from flask import Flask, request, jsonify
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_marshmallow import Marshmallow

from .config import Config

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

# ma = Marshmallow(app)

from . import routes
from app.models import User, Permission, UserPermission
