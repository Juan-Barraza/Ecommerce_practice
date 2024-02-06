from models.product import Product


class Category:
    
    def __init__(self, id: int, name: str, product: Product):
        self.id = id
        self.name = name
        self.product = product