from user import User

def find_user_by_login(users:list,login:str):
    for i in range(len(users)):
        if login == users[i].login:
            return users[i]

def prinimat_chislo(a:int,b:int):
    return a + b


user1 = User("login","123")
user2 = User("login2","223")
users = []
users.append(user1)
users.append(user2)
user_to_find = find_user_by_login(users,"login2")
print(user_to_find.password)
c = prinimat_chislo(10,10)