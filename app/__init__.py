from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

# new new, bring up during optional session
migrate = Migrate(compare_type=True)

def create_app(test_config=None):
    app = Flask(__name__)

    #Consider commenting these two out to discuss database connection
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/desserts_journal'
    
    # Bring up during optional session, used to see what SQL commands SQLAlchemy is using
    app.config['SQLALCHEMY_ECHO'] = True

    # Import models here
    from app.models.dessert import Dessert 

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from .routes import desserts_bp
    app.register_blueprint(desserts_bp)

    from .routes import reviews_bp
    app.register_blueprint(reviews_bp)

    return app

