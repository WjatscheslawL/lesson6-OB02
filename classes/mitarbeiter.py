class Users:
    def __init__(self, user_id, level, name):
        self.__private_ID = user_id
        self.__private_level = level
        self.__private_name = name
        self.__private_active = True

    def get_private_id(self):
        return self.__private_ID

    def get_private_level(self):
        return self.__private_level

    def get_private_name(self):
        return self.__private_name

    def get_private_active(self):
        return self.__private_active

    def set_private_level(self, value):
        self.__private_level = value

    def set_private_name(self, value):
        self.__private_name = value

    def set_private_active(self, value):
        self.__private_active = value


class Admins(Users):
    def __init__(self, user_id, level, name, admins):
        super().__init__(user_id, level, name)
        self.__private_admins = admins

    def get_admins(self):
        return self.__private_admins

    def add_user(self, user_id, name, level):
        if self.get_admins():
            user = Users(user_id, level, name)
            return user

    def _protected_remove_user(self, user_id):
        if user_id == self.get_private_id():
            self.active = False
            print(f"User {user_id} : {self.get_private_name()} was removed")
        else:
            print(f"User {user_id} is note found")

    def delete_user(self, user_id, mb = []):
        for user in mb:
            if user_id == user.get_private_id():
                user.set_private_active(False)
                print(f"User {user.get_private_name()} was removed")
