from app import db
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String)
    rating = db.Column(db.String)
    dateTime = db.Column(db.DateTime)

    def to_dict(self):
        return {
            "description": self.description,
            "rating": self.rating,
            "datetime": self.dateTime
        }

    