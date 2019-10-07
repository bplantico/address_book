from datetime import datetime
from app import db

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    address = db.Column(db.String(120))
    city = db.Column(db.String(60))
    state = db.Column(db.String(60))
    zip = db.Column(db.String(10))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Address {}, {}, {}, {}, {}, {}, {}>'.format(self.id, self.name, self.address, self.city, self.state, self.zip, self.timestamp)
