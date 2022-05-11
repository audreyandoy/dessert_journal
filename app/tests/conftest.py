from flask import request_finished
from app import db
import pytest
from app.models.dessert import Dessert

from app import create_app

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender,response, **extra):
        db.session.remove()
    
    with app.app_context():
        db.create_all() 
        yield app
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_desserts(app):
    bubble_tea = Dessert(id=1, name="Taro Bubble Tea", description="Taro flavored bubble tea with tapioca pearls")
    chocolate_cake = Dessert(id=2, name="Chocolate Cake", description="Decadent chocolate cake")

    db.session.add(bubble_tea)
    db.session.add(chocolate_cake)
    db.session.commit()