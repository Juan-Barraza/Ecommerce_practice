class User:
    
    def __init__(self, id_user: int, names: str, email: str, password: str, registrationDate: str):
        self.id_user = id_user
        self.names = names
        self.email = email
        self.password = password
        self.registrationDate = registrationDate
    
    def show(self):
        pass
