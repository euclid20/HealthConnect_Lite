from flask import jsonify

from models.user_model import User


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

def store_user():
    return "store user endpoint"
