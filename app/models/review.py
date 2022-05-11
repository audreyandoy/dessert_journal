from app import db
class Review(db.Model):
    description = db.Column(db.String)
    rating = db.Column(db.String)
    dateTime = db.Column(db.DateTime)

    def to_dict(self):
        return {
            "description": self.description,
            "rating": self.rating,
            "dateTime": self.dateTime
        }

    