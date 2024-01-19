from models.product import Product


class Fragile_products(Product):
    
    def information(self):
        print("The prduct: " , self.get_name() , " is fragile")

class Perishable_products(Product):
    
    def information(self):
        print("The prduct: ", self.get_name() ,"is perishable")
    

class Special_products(Product):
    
    def information(self):
        print("The prduct: " , self.get_name() ,"is speciial")


product1 = Perishable_products("Sugar", 60,"good quality", 5)
product2 = Special_products("Whisky", 700,"good quality", 2)
product3 = Fragile_products("Windows", 200,"good quality", 3)