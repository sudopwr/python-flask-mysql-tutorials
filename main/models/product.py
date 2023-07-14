from dataclasses import dataclass
from main.extensions import db

@dataclass
class Product(db.Model):
    id: str = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(120), nullable=False)
    description: str = db.Column(db.String(500), nullable=False)
    image: str = db.Column(db.Text, nullable=False)
    price: int = db.Column(db.Double, nullable=False)
    quantity: int = db.Column(db.Integer, nullable=False)

    def __init__(self, name, description, image, price, quantity):
        self.name = name
        self.description = description
        self.image = image
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return '<product %r>' % self.name
