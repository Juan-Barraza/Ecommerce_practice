from models.product import Product
from patterns.decorators import singleton


@singleton
class Cart:
    
    def __init__(self):
        self.products = [
            {"name": "whisky", "price": 400, "description": "whisky of good quality", "quantity": 2 }
        ]
    
    def add(self, product: Product ):
        self.products.append(product)
    
    def delete(self, product: Product):
        self.products.remove(product)
    
    def clear(self, product: Product):
        self.products.clear(product)
        
    def taxes(self):
        total_taxes = 0
        for product in self.products:
            total_taxes += product.taxes()
        return total_taxes

products = [
    {"name": "whisky", "price": 400, "description": "whisky of good quality", "quantity": 2 }
]