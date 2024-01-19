from models.cart import Cart


class User:
    
    def __init__(self, name: str, address: str):
        self.orders = []
        self.name = name
        self.address = address
    
    def add(self, order: Cart ):
        self.orders.append(order)
    
    def show(self):
        for order in self.orders:    
            print("Shopping of history:  {self.orders}")
    
    def taxes(self):
        total_taxes = 0
        for order in self.orders:
            total_taxes += order.taxes()
        return total_taxes