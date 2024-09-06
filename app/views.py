from flask import Blueprint, jsonify, request, session
from .schemas import VoucherSchema
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from .models import User, Vouchers
views = Blueprint('views', __name__)
@views.route('/', methods=['GET'])
def main():
    plain_password = "password"
    hashed = generate_password_hash(plain_password)
    checking = check_password_hash(hashed, plain_password)
    print(checking)
    return jsonify({
        'message' : 'hello! it work!!! congrats'
    })
@views.route('/api/register', methods=['POST'])
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
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'message': 'Email already taken'}), 400 
    hashed_password = generate_password_hash(password,salt_length=16)
    new_user = User(firstname=firstname, lastname=lastname, email=email, password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        'message' : 'User created successfully'
    }), 201

@views.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password= data.get('password')

    if not email or not password:
        return jsonify({
            'message': 'Missing email or password'
        }), 400
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({
            'message' : 'Invalid email'
        }), 401
    if not user.check_password(password):
        return jsonify({
            'message': 'wrong password'
        }), 401
    session[user.id] = user.id 

    return jsonify({
        'message': 'Logged in successfully'
    }), 200

@views.route('/api/logout', methods=['GET'])
def logout():
    session.pop('user_id', None)
    return jsonify({
        'message': 'logged out successfully'
    }), 200

@views.route('/users', methods =['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.__dict__ for user in users])

@views.route('/api/vouchers', methods =['GET'])
def get_vouchers():
    vouchers = Vouchers.query.all()
    voucher_schema = VoucherSchema(many=True)
    vouchers_data = voucher_schema.dump(vouchers)
    return jsonify(vouchers_data)