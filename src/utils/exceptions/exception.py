class UserNotExist(Exception):
    pass

class ProductNotFound(Exception):
   pass

class CategoryNotFound(Exception):
     pass
 
class DatabaseConnectionError(Exception):
     pass
 
class DatabaseQueryError(Exception):
    pass

class ExistingUser(Exception):
     pass

class ErrorCreatedUser(Exception):
     pass 