from models.user import User
from models.product import Product


class Review:
    
    def __init__(self, id_review: int, rating: int, comment: str, created_at: str):
        self.id_review = id_review
        self.rating = rating
        self.comment = comment
        self.created_at = created_at
        
    
    def view(self):
        pass
    
    def date(self):
        print("dd/mm/YYYY HH:MM:S")
    