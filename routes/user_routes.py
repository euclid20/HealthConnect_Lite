from flask import Blueprint

from controllers.user_controller import get_users, store_user
from entities.user_entity import User

user_blueprint = Blueprint('user', __name__, url_prefix='/user');

@user_blueprint.route('/', methods=['GET'])
def get_users_route():
    return get_users()

@user_blueprint.route('/', methods=['POST'])
def store_user_route():
    user = User(
        id=1,
        email="faidfadjri@gmail.com",
        first_name="faid",
        last_name="fadjri",
        avatar="avatar"
    )
    return store_user(user)

