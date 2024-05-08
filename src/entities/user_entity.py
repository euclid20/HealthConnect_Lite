class UserEntity:
    def __init__(self,email, first_name, last_name, avatar = ''):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar

    @classmethod
    def from_db_model(cls, user):
        """
        Create a UserEntity instance from a User database model instance.
        """
        return cls(
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            avatar=user.avatar
        )

    def to_dict(self):
        """
        Convert the UserEntity instance to a dictionary.
        """
        return {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'avatar': self.avatar
        }
