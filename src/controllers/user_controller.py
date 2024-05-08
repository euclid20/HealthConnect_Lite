from flask import jsonify

from models.user_model import User
from entities.user_entity import UserEntity
from config.setup import db


def get_users():
    first_user = User.query.first()
    if first_user:
        return jsonify({
            "id": first_user.id,
            "avatar": first_user.avatar,
            "email": first_user.email
        })
    else:
        return jsonify({"message": "No users found"})

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
