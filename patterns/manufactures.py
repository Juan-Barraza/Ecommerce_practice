from abc import ABC, abstractmethod


class Manufactured_products(ABC):
    
    @abstractmethod
    def generate(self):
        pass


class Product_lightweight(Manufactured_products):
    
    def generate(self):
        print("Product lightweight")


class Product_heavy(Manufactured_products):
    
    def generate(self):
        print("Product heavy")


class Product_refrigerated(Manufactured_products):
    
    def generate(self):
        print("Product refrigerated")


class Create_factory(ABC):
    
    @abstractmethod
    def factory_method(self):
        pass
    
    def create_product(self):
        product = self.factory_method()
        result = product.generate()  
        return result


class Manufactures_a(Create_factory):
    
    def factory_method(self):
        return Product_lightweight()


class Manufactures_b(Create_factory):
    
    def factory_method(self):
        return Product_heavy()


class Manufactures_c(Create_factory):
    
    def factory_method(self):
        return Product_refrigerated()
    

factory_a = Manufactures_a()
product_a = factory_a.create_product()