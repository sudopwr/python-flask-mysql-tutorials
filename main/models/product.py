from main.extensions import db

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
