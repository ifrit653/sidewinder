from flask import Blueprint, jsonify, request
from .schemas import VoucherSchema
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from .models import User, Vouchers
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
views = Blueprint('views', __name__)
@views.route('/', methods=['GET'])
def main():
    return jsonify({
        'message' : 'test'
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
    # hashed_password = generate_password_hash(password)
    new_user = User(firstname=firstname, lastname=lastname, email=email, password=password, role=role)
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
    if not user or not check_password_hash(user.password, password):
        return jsonify({
            'message' : 'Invalid credentials'
        }), 401
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200

''' this logout endpoint use session '''
# @views.route('/api/logout', methods=['GET'])
# def logout():
#     session.pop('user_id', None)
#     return jsonify({
#         'message': 'logged out successfully'
#     }), 200

@views.route('/users', methods =['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.__dict__ for user in users])

@views.route('/api/vouchers', methods=['GET'])
@jwt_required()
def set_vouchers():
    data = request.get_json()
    debit_amount = data.get("debit_amount")
    credit_amount = data.get("credit_amount")
    debit_code = data.get("debit_code")
    credit_code = data.get("credit_code")
    label = data.get('label')
    current_user_id = get_jwt_identity()
    # current_user = User.query.get(current_user_id)
    user_id = current_user_id
    if not debit_amount or not credit_amount or not debit_code or not credit_code or not label or not user_id:
        return jsonify({
            'message' : 'Missing parameters'
        },), 400 
    new_voucher = Vouchers(debit_amount=debit_amount, credit_amount=credit_amount, debit_code=debit_code, credit_code=credit_code, label=label, user_id=user_id)
    db.session.add(new_voucher)
    db.session.commit()

    return jsonify({
        'message' : 'voucher added successfully'
    }), 201


@views.route('/vouchers', methods =['GET'])
def get_vouchers():
    page = request.args.get('page' ,1,type = int)
    per_page = request.args.get('per_page',10, type=int)

    pagination = Vouchers.query.pagination(page=page, per_page = per_page, error_out = False)
    vouchers = pagination.items

    serialized_vouchers = VoucherSchema(many=True).dump(vouchers)

    response = {
        # 'vouchers': [{id: voucher.id, 'debit_amount': voucher.debit_amount, 'credit_amount': voucher.credit_amount, 'debit_code': voucher.debit_code, 'credit_code': voucher.credit_code, 'label': voucher.label}],
        'vouchers': serialized_vouchers,
        'total': pagination.total, 
        'page': pagination.page,
        'pages': pagination.pages,
        'per_page': pagination.per_page,
        'has_next': pagination.has_next,
        'has_prev': pagination.has_prev,
    }
    return jsonify(response)
    # vouchers = Vouchers.query.all()
    # voucher_schema = VoucherSchema(many=True)
    # vouchers_data = voucher_schema.dump(vouchers)
    # return jsonify(vouchers_data)