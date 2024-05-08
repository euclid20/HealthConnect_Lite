from entities.user_entity import User


def get_users():
    return "hello this is a list of users"

def store_user(user: User):
    return user.to_json()