from main.extensions import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.String(80), db.ForeignKey('user.id'), nullable=False)

    def __init__(self, product_id, user_id):
        self.product_id = product_id
        self.user_id = user_id

    def __repr__(self):
        return '<Orders %r>' % self.id
