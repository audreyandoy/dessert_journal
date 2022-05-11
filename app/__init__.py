from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()

# new new, bring up during optional session
migrate = Migrate(compare_type=True)
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)

    #Consider commenting these two out to discuss database connection
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if not test_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")

    db.init_app(app)
    migrate.init_app(app, db)

    # Import models here
    from app.models.dessert import Dessert 
    from app.models.review import Review

    # Register Blueprints here
    from .routes import desserts_bp
    app.register_blueprint(desserts_bp)

    from .routes import reviews_bp
    app.register_blueprint(reviews_bp)

    return app

