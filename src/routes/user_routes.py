from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from src.config.setup import db
from src.models.user_model import User

user_blueprint = Blueprint('user_bp', __name__)

# GET route — list all users
@user_blueprint.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = [
        {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
        for user in users
    ]
    return jsonify(result)

# POST route — register a new user
@user_blueprint.route('/users', methods=['POST'])
def register_user():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    # 🔹 Check for missing fields
    if not all([name, email, password]):
        return jsonify({'error': 'All fields (name, email, password) are required'}), 400

    # 🔹 Validate email format
    if '@' not in email or '.' not in email:
        return jsonify({'error': 'Invalid email format'}), 400

    # 🔹 Validate password length
    if len(password) < 6:
        return jsonify({'error': 'Password must be at least 6 characters'}), 400

    # 🔹 Check for duplicate email
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already exists'}), 409

    # 🔐 Hash the password
    hashed_password = generate_password_hash(password)

    # 🔹 Create and save user
    new_user = User(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201