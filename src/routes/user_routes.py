import os
from flask import Blueprint, request, jsonify
from controllers.user_controller import get_users, store_user, get_specific_user, update_user, delete_user
from entities.user_entity import UserEntity
from dotenv import load_dotenv
import requests
load_dotenv()

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

@user_blueprint.route('/', methods=['PUT'])
def update_user_route():

    # Check if the request contains form data
    if not request.form:
        return jsonify({'message': 'Unprocessable content', 'error': 'No data provided'}), 422

    user_id = request.form.get('user_id')
    if not user_id:
        return jsonify({'message': 'Unprocessable content', 'error': 'user_id is not defined as payload'}), 422

    # Get other form fields
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    if not (email and first_name and last_name):
        return jsonify({'message': 'Unprocessable content', 'error': 'Missing required fields'}), 422
    
    user = UserEntity(email, first_name, last_name)

    # Call the controller function to update the user
    return update_user(user_id, user)

@user_blueprint.route('/', methods=['DELETE'])
def delete_user_route():

    # Header validation
    if not request.headers.get('Authorization'):
        return jsonify({'message': 'Unauthorized', 'error': 'You are not allowed to delete user'}), 403


    authorization_header = request.headers.get('Authorization')

    if authorization_header != os.getenv("AUTHORIZATION_KEY"):
        return jsonify({'message': 'Forbidden, failed key', 'error': 'You are not allowed to delete user'}), 403

    # Check if the request contains form data
    if not request.form:
        return jsonify({'message': 'Unprocessable content', 'error': 'No data provided'}), 422
    
    user_id = request.form.get('user_id')
    if not user_id:
        return jsonify({'message': 'Unprocessable content', 'error': 'user_id is not defined as payload'}), 422
    
    return delete_user(user_id)

@user_blueprint.route('/fetch', methods=['GET'])
def fetching_user():
    # Check if the 'page' parameter is included in the request
    page = request.args.get('page')
    if not page:
        return jsonify({'message': 'Bad request', 'error': 'Missing parameter: page'}), 400
    
    # Make a GET request to the API endpoint
    api_url = f"https://reqres.in/api/users?page={page}"
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Iterate over each user in the 'data' property
        for user_data in data['data']:
            # Extract user data

            user_id = user_data['id']
            avatar = user_data['avatar']
            email = user_data['email']
            first_name = user_data['first_name']
            last_name = user_data['last_name']
            
            # Create UserEntity instance
            user_entity = UserEntity(id=user_id, avatar=avatar, email=email, first_name=first_name, last_name=last_name)
            
            # Store the user in the database
            store_user(user_entity)
        
        return jsonify({'message': 'Users stored successfully'}), 200
    else:
        # If the request was not successful, return an error message
        return jsonify({'message': 'Failed to fetch data from the API'}), response.status_code