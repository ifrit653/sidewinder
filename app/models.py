from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
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