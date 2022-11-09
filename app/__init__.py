from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

load_dotenv()
db = SQLAlchemy()

# new new, bring up during optional session
migrate = Migrate(compare_type=True)

def create_app(test_config=None):
    app = Flask(__name__)

    #Consider commenting these two out to discuss database connection
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    
    # Bring up during optional session, used to see what SQL commands SQLAlchemy is using
    app.config['SQLALCHEMY_ECHO'] = True

    # Import models here
    from app.models.dessert import Dessert
    from app.models.review import Review 
 

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from .routes import desserts_bp
    app.register_blueprint(desserts_bp)

    return app

