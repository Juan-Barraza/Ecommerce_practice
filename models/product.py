class Product:
    
    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity
        
    def toJson(self):
        return {
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "quiantity": self.quantity
        }

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_description(self):
        return self.description
    
    def get_quantity(self):
        return self.quantity
    
    def set_name(self, now_name):
        self.name = now_name
    
    def set_price(self, now_price):
        self.price = now_price
    
    def set_description(self, now_description):
        self.description = now_description
    
    def set_quantity(self, now_quantity):
        self.quantity = now_quantity
        
    def taxes(self):
        tax = self.price * 0.19
        total = self.price + tax
        return total
    
prod = [
    {"name": "whisky", "price": 400, "description": "whisky of good quality", "quantity": 2 },
    {"name": "beer", "price": 30, "description": "beer of good quality", "quantity": 10 },
    {"name": "water", "price": 10, "description": "water of good quality", "quantity": 20 }
]