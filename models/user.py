class User:
    """Модель пользователя"""
    def __init__(self,login:str,password:str):
        self.login = login
        self.password = password