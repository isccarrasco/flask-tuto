from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from project import views
from project import api

application = Flask(__name__)
application.config.from_object('config')

# Instance of ORM
database = SQLAlchemy(application)

# Instance of WS
ws_api = Api(application)

