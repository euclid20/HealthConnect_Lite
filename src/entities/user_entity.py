class UserEntity:
    def __init__(self, email, first_name, last_name, avatar='', id=None):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar
