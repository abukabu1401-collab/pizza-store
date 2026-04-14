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
    
def authorization(self):
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    
    for i in range(len(self.users)):
        if login == self.users[i].login and password == self.users[i].password:
            print("Авторизация успешна")
            return self.users[i]
    
    print("Неверный логин или пароль")
    
def add_new_user(self, user: User):
    if user.login == "":
        print("Логин не может быть пустым")
        return

    if user.password == "":
        print("Пароль не может быть пустым")
        return

    for i in range(len(self.users)):
        if self.users[i].login == user.login:
            print("Пользователь с таким логином уже существует")
            return

    self.users.append(user)
    print("Пользователь успешно добавлен")