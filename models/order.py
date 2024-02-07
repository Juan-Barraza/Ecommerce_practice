from models.user import User

class Order:
    
    def __init__(self, id_order: int, user: User, total_price: int, created_at: str):
        self.id_order = id_order
        self.user = user
        self.total_price = total_price
        self.created_at = created_at