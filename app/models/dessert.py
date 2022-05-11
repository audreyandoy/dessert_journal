from app import db

class Dessert(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

    def update(self, req_body):
        self.name = req_body["name"]
        self.description = req_body["description"]

    #include way to refactor using a class method