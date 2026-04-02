class Person:
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city


class PersonRepository:
    def __init__(self):
        self.persons = []

    def add_person(self, person: Person):
        self.persons.append(person)

    def find_by_name(self, name: str):
        for i in range(len(self.persons)):
            if self.persons[i].name == name:
                print(self.persons[i].name, self.persons[i].age, self.persons[i].city)

    def find_by_age(self, age: int):
        for i in range(len(self.persons)):
            if self.persons[i].age == age:
                print(self.persons[i].name, self.persons[i].age, self.persons[i].city)

    def find_by_city(self, city: str):
        for i in range(len(self.persons)):
            if self.persons[i].city == city:
                print(self.persons[i].name, self.persons[i].age, self.persons[i].city)

    def update_person_name(self, old_name: str, new_name: str):
        for i in range(len(self.persons)):
            if self.persons[i].name == old_name:
                self.persons[i].name = new_name
                print(self.persons[i].name, self.persons[i].age, self.persons[i].city)

person1 = Person("Никита",13,"Нижний-Новгород")
person2 = Person("Дмитрий",25,"Москва")
person3 = Person("Иван",17,"Санкт-Петербург")
repository = PersonRepository()
repository.add_person(person1)
repository.add_person(person2)
repository.add_person(person3)
repository.find_by_city("Москва")
repository.update_person_name("Дмитрий","Даниил")