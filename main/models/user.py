from main.extensions import db

class User(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    address = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=False)

    def __init__(self, id, name, email, address, image):
        self.id = id
        self.name = name
        self.email = email
        self.address = address
        self.image = image

    def __repr__(self):
        return '<User %r>' % self.id
