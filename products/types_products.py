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