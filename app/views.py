from flask import render_template, jsonify, current_app as app
from .models import User

@app.route('/users', methods =['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.__dict__ for user in users])