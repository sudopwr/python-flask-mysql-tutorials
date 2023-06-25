import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from main.extensions import db
from main.config import config
from main.modules.products import products_api_bpl 
from main.modules.routes import register_route

app = Flask(__name__)
app.config.from_object(config.get(os.getenv("APP_MODE")))
db.init_app(app)
register_route(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    address = db.Column(db.String(200), nullable=False)

    def __init__(self, username, email, address):
        self.username = username
        self.email = email
        self.address = address

    def __repr__(self):
        return '<User %r>' % self.username

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Double, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, name, description, image, price, quantity):
        self.name = name
        self.description = description
        self.image = image
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return '<product %r>' % self.name

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    product = db.relationship('product', foreign_keys = 'order.product_id')
    user = db.relationship('user', foreign_keys = 'order.user_id')

    def __init__(self, product_id, user_id):
        self.product_id = product_id
        self.user_id = user_id

    def __repr__(self):
        return '<Orders %r>' % self.id

with app.app_context():
    db.create_all()
