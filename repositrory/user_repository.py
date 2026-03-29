from models.user import User
class UsersRepository:
    """Хранилище пользователя"""
    def __init__(self):
        self.users = []
        
    def add_new_user(self,user:User)->bool:
        self.users.append(user)
        
    def find_user_by_login(self,login:str)->None:
        for i in range(len(self.users)):
            if login == self.users[i]:
                login = self.users[i]