import enum

from models.cart import Cart
from models.user import User
from datetime import datetime


class State(enum.Enum):
    WAIT = "Wait"
    IN_PROGRESS = "In progress"
    PAID = "Paid"
    CANCEL = "Cancel"

class Order:
    
    def init(self):
        self.state = State.WAIT 
        self.current_date = datetime.now()
    
    def information(self):
        for product in self.products:
            print("The products are: {self.products}")
            print("The date and time: {self.current_date}")
        
    def paid(self):
        total_paid = 0
        for order in self.orders:
            total_paid += order.taxes()
        return total_paid 
    
    def update(self, new_state: State):
        self.state = new_state
        
    def view_status(self):
       self.state.value