from flask import jsonify

from models.user_model import User
from entities.user_entity import UserEntity
from config.setup import db


def get_users():
    # Get all users from the database
    users = User.query.all()
    if users:
        # Serialize each user and store them in a list
        serialized_users = []
        for user in users:
            serialized_users.append({
                "id": user.id,
                "avatar": user.avatar,
                "email": user.email
            })
        # Return the list of serialized users
        return jsonify(serialized_users)
    else:
        return jsonify({"message": "No users found"})
    
def get_specific_user(user_id: int):
    user = User.query.filter_by(id=user_id).first()
    if user:
        # Serialize the user and return it
        serialized_user = {
            "id": user.id,
            "username" : f'{user.first_name}{user.last_name}'.lower(),
            "avatar": user.avatar,
            "email": user.email,
        }
        return jsonify(serialized_user)
    else:
        return jsonify({"message": "User not found"})


def update_user(user_id, user: UserEntity):
    # Retrieve the user from the database
    user_to_update = User.query.get(user_id)
    if user_to_update:
        # Update the user's attributes with the new data
        user_to_update.email = user.email
        user_to_update.first_name = user.first_name
        user_to_update.last_name = user.last_name

        # Commit the changes to the database
        try:
            db.session.commit()
            return jsonify({'message': 'User updated successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': f'Failed to update user: {str(e)}'}), 500
    else:
        return jsonify({'message': 'User not found'}), 404


def store_user(user_data: UserEntity):

    if user_data.id is not None:
        existing_user = User.query.filter_by(id=user_data.id).first()
        if existing_user:
            return jsonify({'message': 'User already exists. Data has been saved.'}), 200



    # If the user does not exist, create a new user
    new_user = User(email=user_data.email, first_name=user_data.first_name, last_name=user_data.last_name, avatar=user_data.avatar)
    db.session.add(new_user)

    try:
        # Commit the transaction to save the new user to the database
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        # If there's an error, rollback the transaction
        db.session.rollback()
        return jsonify({'error': f'Failed to create user: {str(e)}'}), 500

def delete_user(user_id):
    # Retrieve the user from the database
    user_to_delete = User.query.get(user_id)
    if user_to_delete:
        # Delete the user from the database
        try:
            db.session.delete(user_to_delete)
            db.session.commit()
            return jsonify({'message': 'User deleted successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': f'Failed to delete user: {str(e)}'}), 500
    else:
        return jsonify({'message': 'User not found'}), 404
