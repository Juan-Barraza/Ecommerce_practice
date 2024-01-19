from abc import ABC, abstractmethod


class Office (ABC):
    
    @abstractmethod
    def dispatch(self):
        pass

class Normal_office(Office):
    
    def dispatch(self):
        print("the product was dispatched")
        print("will arrive in 3 days ")
        
class Express_office(Office):
    
    def dispatch(self):
        print("the product was dispatched")
    
    def advance_clearance(self):
        print("the product was shipped a little faster and arrived early")
    
class Back_office(Office):
    
    def dispatch(self):
        print("the product will be dispatched soon")
    
    def delay(self):
        print("the dispatch is delayed by internal problems")