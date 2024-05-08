import os
from flask import Blueprint, request, jsonify
from controllers.user_controller import get_users, store_user, get_specific_user
from entities.user_entity import UserEntity

user_blueprint = Blueprint('user', __name__, url_prefix='/user')

@user_blueprint.route('/', methods=['GET'])
def get_users_route():
    return get_users()

@user_blueprint.route('/<int:user_id>', methods=['GET'])
def get_specific_user_route(user_id):
    return get_specific_user(user_id)

@user_blueprint.route('/', methods=['POST'])
def store_user_route():
    # Check if the request contains a file
    if 'avatar' not in request.files:
        return jsonify({'message': 'Unprocessable content', 'error': 'Avatar is missing / not a file'}), 422


    # Handle uploading avatar file
    avatar = request.files['avatar']
    avatar_filename = avatar.filename

    if avatar_filename == '':
        return jsonify({'message': 'Unprocessable content', 'error': 'Avatar file is empty'}), 422

    upload_dir = 'public/images'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    avatar_path = os.path.join(upload_dir, avatar.filename)
    avatar.save(avatar_path)

    # Get other form fields
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    # Validation
    if not (email and first_name and last_name):
        return jsonify({'message': 'Unprocessable content', 'error': 'Missing required fields'}), 422

    # Create UserEntity instance
    user_data = UserEntity(avatar=avatar_filename, email=email, first_name=first_name, last_name=last_name)

    # Call the controller function to store the user
    return store_user(user_data)

