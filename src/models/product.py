from models.category import Category

class Product:
    
    def __init__(self, id: int, category_id: Category, name: str, price: int, description: str, size: str, color: str, quantity: int):
        self.id = id
        self.category_id = category_id
        self.name = name
        self.price = price
        self.description = description
        self.size = size
        self.color = color
        self.quantity = quantity