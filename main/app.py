import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from main.extensions import db
from main.config import config
from main.usecases import register_route
from main.models import *

app = Flask(__name__)
app.config.from_object(config.get(os.getenv("APP_MODE")))
db.init_app(app)
register_route(app)

with app.app_context():
    db.create_all()
