from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import fields
from flask_marshmallow import Marshmallow 
from .models import User, Vouchers, db
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

class VoucherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Vouchers
        load_instance = True
        include_fk = True
        sqla_session = db.session
    id = auto_field()
    debit_amount = auto_field()
    credit_amount = auto_field()
    debit_code = auto_field()
    credit_code = auto_field()
    label = auto_field()
    user_id = auto_field()
    user = ma.Nested(UserSchema)