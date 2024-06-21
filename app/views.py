from flask import Blueprint, jsonify, current_app, request, session as app
from .models import User, Vouchers, db
from .schemas import VoucherSchema
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    email = data.get('email')
    password = data.get('password')
    role = 'user'

    if not firstname or not lastname or not password or not email:
        return jsonify({
            'message' : 'Missing parameters'
        },), 400 
    hashed_password = generate_password_hash(password)
    new_user = User(firstname=firstname, lastname=lastname, email=email, password_hash=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        'message' : 'User created successfully'
    }), 201

@auth.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password= data.get('password')

    if not email or not password:
        return jsonify({
            'message': 'Missing email or password'
        }), 400
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({
            'message' : 'Invalid credentials'
        }), 401
    session[user.id] = user.id 

    return jsonify({
        'message': 'Logged in successfully'
    }), 200

@auth.route('api/logout', methods=['GET'])
def logout():
    session.pop('user_id', None)
    return jsonify({
        'message': 'logged out successfully'
    }), 200

@auth.route('/users', methods =['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.__dict__ for user in users])

@auth.route('/api/vouchers', methods =['GET'])
def get_vouchers():
    vouchers = Vouchers.query.all()
    voucher_schema = VoucherSchema(many=True)
    vouchers_data = voucher_schema.dump(vouchers)
    return jsonify(vouchers_data)