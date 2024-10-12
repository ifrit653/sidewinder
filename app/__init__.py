from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    from .views import views

    app.register_blueprint(views)
    app.config.from_object(Config)
    jwt = JWTManager(app)
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    #JWT Blacklist configuration
    @jwt.token_in_blocklist_loader  
    def isTokenExpired_callback(jwt_header, jwt_payload):
        from app.helpers import isTokenExpired 
        jti = jwt_payload['jti']
        return isTokenExpired(jti)
    with app.app_context():
        from . import views, models 

        # db.create_all()
    return app 


