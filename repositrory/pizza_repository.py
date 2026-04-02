from models.pizza import Pizza
class PizzaRepository:
    """Хранилице пицц"""
    def __init__(self):
        self.pizzas = []

    def get_all_pizzas(self)->list:
        """Возвращает список всех пицц"""
        return self.pizzas.copy()
    
    def get_pizza_count(self)->int:
        """Возвращает количество пицц"""
        return len(self.pizzas)
    
    def add_pizza(self,pizza:Pizza)->None:
        """Добавляет пиццу"""
        self.pizzas.append(pizza)
        
    def add_pizza_by_parameters(self,name:str,price:int,ingridientes:list,size:int)->None:
        """Добавляет пиццу по параметрам"""
        pizza = Pizza(name,price,ingridientes,size)
        self.pizzas.append(pizza)

    def delete_pizza_by_name(self,name:str)->None:
        """Удаление пиццы"""
        for i in range(len(self.pizzas)):
            if self.pizzas[i].name == name:
                self.pizzas.remove(self.pizzas[i])
                
    def delete_all_pizzas(self)->None:
        """Удаляет все пиццы"""
        self.pizzas.clear()
        
    def update_pizza_by_name(self):
        name_pizza = input("Введите имя пиццы: ")
        new_name = input("Введите новое имя пиццы: ")

        for i in range(len(self.pizzas)):
            if name_pizza == self.pizzas[i].name:
                self.pizzas[i].name = new_name
                
    def sort_by_price(self)->None:
        self.pizzas.sort(key=lambda pizza: pizza.price)

    def sort_by_name(self)->None:
        self.pizzas.sort(key=lambda pizza: pizza.name)

    def sort_by_size(self)->None:
        self.pizzas.sort(key=lambda pizza: pizza.size)
        
    def sort_by_price_from_max_to_mine(self)->None:
        self.pizzas.sort(key=lambda pizza: pizza.price,reverse=True)