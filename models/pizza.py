class Pizza:
    """Модель пиццы"""
    def __init__(self,name:str,price:int,ingridientes:list,size:int):
        self.name = name
        self.price = price
        self.ingridientes = ingridientes
        self.size = size
        