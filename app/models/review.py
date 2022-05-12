from app import db
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String)
    rating = db.Column(db.String)
    dateTime = db.Column(db.DateTime)
    dessert_id = db.Column(db.Integer, db.ForeignKey('dessert.id'))
    dessert = db.relationship("Dessert", back_populates="reviews")
    # dessert_reviews = db.relationship("Dessert", backref='desserts')

    def to_dict(self):
        return {
            "description": self.description,
            "rating": self.rating,
            "datetime": self.dateTime
        }

    