from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from flask_jwt_extended import JWTManager, create_access_token

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    from .views import views
    app.register_blueprint(views)
    app.config.from_object(Config)
    jtw = JWTManager(app)
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    with app.app_context():
        from . import views, models 
        # db.create_all()
    return app 