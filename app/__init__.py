from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

# new new, bring up during optional session
migrate = Migrate(compare_type=True)

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/dessert_journal'
    
    # new new, bring up during optional session
    app.config['SQLALCHEMY_ECHO'] = True

    # Import models here
    from app.models.dessert import Dessert 

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from .routes import desserts_bp
    app.register_blueprint(desserts_bp)

    return app

