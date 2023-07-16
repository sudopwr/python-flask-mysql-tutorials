from main.extensions import db
from dataclasses import dataclass
import datetime

@dataclass
class Order(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    product_id: int = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id: int = db.Column(db.String(80), db.ForeignKey('user.id'), nullable=False)
    quantity: int = db.Column(db.Integer, nullable=False)
    status: str = db.Column(db.String(100), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Orders %r>' % self.id
