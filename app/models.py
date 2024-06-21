from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(50), nullable = False)
    lastname = db.Column(db.String(50), nullable = False) 
    role = db.Column(db.String(50))
    email = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.String(64), nullable = False)

    def __init__(self, firstname, lastname, password, email, role):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.role = role
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return f'<User {self.email}>'
class Code_debit(db.Model):
    __tablename__ = 'Code_debit'
    code_debit= db.Column(db.String(11), primary_key= True)
    budget = db.Column(db.Float, nullable=False)

    def __init__(self, code_debit, budget):
        self.code_debit = code_debit
        self.budget = budget

    def __repr__(self):
        return f'Code_debit {self.code_debit}'
class Vouchers(db.Model):
    __tablename__ = 'vouchers'
    id = db.Column(db.Integer, primary_key= True)
    debit_amount = db.Column(db.Float, nullable = False)
    credit_amount = db.Column(db.Float, nullable = False)
    debit_code = db.Column(db.String(11),db.ForeignKey(Code_debit.code_debit), nullable = False)
    credit_code = db.Column(db.String(11), nullable = False)
    label = db.Column(db.String(255), nullable = False)
    user_id= db.Column(db.Integer, db.ForeignKey(User.id))


    def __init__(self, debit_amount, credit_amount, debit_code, credit_code, label, user_id):
        self.debit_amount = debit_amount
        self.credit_amount = credit_amount
        self.debit_code = debit_code
        self.credit_code = credit_code
        self.label = label
        self.user_id = user_id
    
        def __repr__(self):
            return f'<Voucher {self.label}>'
        


