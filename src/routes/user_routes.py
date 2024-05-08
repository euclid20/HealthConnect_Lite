from flask import Blueprint, request, jsonify

from controllers.user_controller import get_users, store_user
from entities.user_entity import UserEntity


user_blueprint = Blueprint('user', __name__, url_prefix='/user');

@user_blueprint.route('/', methods=['GET'])
def get_users_route():
    return get_users()

@user_blueprint.route('/', methods=['POST'])
def store_user_route():

    form  = request.form

    # Validation

    # Define the required fields
    required_fields = ['email', 'first_name', 'last_name', 'avatar']
    
    # Check for missing fields
    missing_fields = [field for field in required_fields if field not in form]

    if missing_fields:
        return jsonify({'message': 'Unprocessable content', 'error': f'Missing fields: {", ".join(missing_fields)}'}), 422    

    email = form['email']
    first_name = form['first_name']
    last_name = form['last_name']
    avatar = form['avatar']

    # Create UserEntity instance
    user_data = UserEntity(avatar=avatar, email=email, first_name=first_name, last_name=last_name)
    return store_user(user_data)   