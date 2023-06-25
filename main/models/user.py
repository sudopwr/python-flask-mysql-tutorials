from main.extensions import db

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
