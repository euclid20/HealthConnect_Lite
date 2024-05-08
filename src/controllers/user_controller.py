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
            "avatar": user.avatar,
            "email": user.email
        }
        return jsonify(serialized_user)
    else:
        return jsonify({"message": "User not found"})


def store_user(user_data: UserEntity):
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
