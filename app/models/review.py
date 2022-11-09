from app import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    dateTime = db.Column(db.DateTime)
    would_order_again = db.Column(db.String)
    
