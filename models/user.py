class User:
    """Модель пользователя"""
    def __init__(self,login:str,password:str):
        self.login = login
        self.password = password
        
    def __str__(self)->str:
        return f"Пользователь {self.login},пароль {self.password}"