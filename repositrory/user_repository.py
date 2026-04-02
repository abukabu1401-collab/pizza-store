from models.user import User
class UserRepository:
    """Хранилище пользователя"""
    def __init__(self):
        self.users = []
        
    def add_new_user(self,user:User):
        self.users.append(user)
        
    def find_user_by_login(self,login:str):
        for i in range(len(self.users)):
            if login == self.users[i].login:
                return self.users[i]

    def update_user_login(self,old_login:str,new_login:str):
        for i in range(len(self.users)):
            if old_login == self.users[i].login:
                self.users[i].login = new_login
                return self.users[i]

    def delete_user_by_login(self,login:str):
        for i in range(len(self.users)):
            if login == self.users[i].login:
                self.users.remove(self.users[i])
                
    def get_all_users(self)->list:
        return self.users.copy()