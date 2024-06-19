from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from flask_marshmallow import Marshmallow 
from .models import User
from app import create_app 
from werkzeug.security import generate_password_hash

app = create_app
ma = Marshmallow(app)
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True
    
    password = fields.Method('load_password',deserialize="load_password")
    def load_password(self, value):
        return generate_password_hash(value) 
