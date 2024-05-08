class User:
    def __init__(self, id, email, first_name, last_name, avatar, created_at=None, updated_at=None, deleted_at=None):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at

    def __repr__(self):
        return f"User(id={self.id}, email='{self.email}', first_name='{self.first_name}', " \
               f"last_name='{self.last_name}', avatar='{self.avatar}', created_at='{self.created_at}', " \
               f"updated_at='{self.updated_at}', deleted_at='{self.deleted_at}')"

    def to_json(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "avatar": self.avatar,
            "created_at": str(self.created_at) if self.created_at else None,
            "updated_at": str(self.updated_at) if self.updated_at else None,
            "deleted_at": str(self.deleted_at) if self.deleted_at else None
        }
