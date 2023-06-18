from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from extensions import db


def create_app():
    app = Flask(__name__)
    db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


with app.app_context():
    admin = User('admin', 'admin@example.com')

    # In case user table doesn't exists already. Else remove it.
    db.create_all()

    db.session.add(admin)

    db.session.commit()  # This is needed to write the changes to database

    User.query.all()

    User.query.filter_by(username='admin').first()
