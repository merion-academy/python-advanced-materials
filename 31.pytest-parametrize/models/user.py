import hashlib


def hash_password(value: str):
    return hashlib.sha256(value.encode()).hexdigest()


def password_validator(pwd, hashed):
    hashed_pwd = hash_password(pwd)
    return hashed_pwd == hashed


class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = None
        self.password = password

    @property
    def email(self):
        return f"{self.username.lower()}@example.com"

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if value is not None:
            value = hash_password(value)
        self.__password = value

    @password.deleter
    def password(self):
        self.__password = None
