from models.product import Product
from models.cart import Cart
from models.user import User
from models.order import Order
from products.types_products import *
from patterns.manufactures import *
from exeptions.exceptions import SinStockException,PagoRechazadoException,DespachoFallidoException


class Main(object):
    pass
    



print(product2.get_name())
print(product1.taxes())
product_a