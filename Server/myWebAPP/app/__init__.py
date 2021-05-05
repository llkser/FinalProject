from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
import datetime

app = Flask(__name__)
app.config.from_object('config')

from app import views