class UserNotExist(Exception):
    pass

class ProductNotFound(Exception):
     def __init__(self, message):
        super().__init__(message)
        self.message = message
     
     def to_dict(self):
        return {"error_message": str(self)}

class CategoryNotFound(Exception):
     pass
 
class DatabaseConnectionError(Exception):
     pass

class ExistingUser(Exception):
     pass

class ErrorCreatedUser(Exception):
     pass

class ErrorCreatedCategory(Exception):
     pass