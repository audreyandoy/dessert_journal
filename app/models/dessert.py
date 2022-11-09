from app import db

class Dessert(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    dessert_type = db.Column(db.String)
    cost = db.Column(db.Float, default=None)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

    def update(self, req_body):
        self.name = req_body["name"]
        self.description = req_body["description"]
    
    @classmethod
    def from_dict(cls, req_body):
        return cls(
            name=req_body["name"],
            description=req_body["description"]
        )

    #include way to refactor using a class method