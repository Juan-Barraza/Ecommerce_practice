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
        
    def get_productId(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_description(self):
        return self.description
    
    def get_size(self):
        return self.size
    
    def get_color(self):
        return self.color
    
    def get_quantity(self):
        return self.quantity
    
    def set_name(self, now_name):
        self.name = now_name
    
    def set_price(self, now_price):
        self.price = now_price
    
    def set_description(self, now_description):
        self.description = now_description
    
    def set_size(self, now_size):
        self.size = now_size
    
    def set_color(self, now_color):
        self.color = now_color
    
    def set_quantity(self, now_quantity):
        self.quantity = now_quantity
        
    def taxes(self):
        tax = self.price * 0.19
        total = self.price + tax
        return total
products = []