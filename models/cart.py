from models.product import Product
from patterns.decorators import singleton


@singleton
class Cart:
    
    def __init__(self):
        self.products = []
    
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
    
    
#cart1 = Cart()
#cart2 = Cart()
#if __name__ == '__main__':
    
    #cart1.add(Product(name = "Whiskey", price = 50000, description = "Good quality", quantity = 2))
    #cart2.add(Product(name = "Vino", price = 200000, description = "good", quantity = 3))

    #print(cart1.products)
    #print(cart2.products)