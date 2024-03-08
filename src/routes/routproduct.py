from flask import Blueprint, jsonify, views
from src.services.product import Product
from src.utils.exceptions.exception import ProductNotFound

prod = Blueprint('produc_blueprint', __name__)

class ProductView(views.MethodView):
    
    def get(self):
        
        
        try:
            product = Product.getProducts()
            category = Product.getCategoryPro()
            
            if (not category):
                return jsonify({"message": "Error" })
                             
            infoCategory = {
                "id": [0],
                "name": [1]
                }
            products = []
            for prod in product:  # type: ignore
                product_info = {
                    "id": prod[0], 
                    "category": infoCategory,
                    "name": prod[2],
                    "price": prod[3],
                    "description": prod[4],
                    "size": prod[5],
                    "color": prod[6],
                    "quantity": prod[7]
                    }
                products.append(product_info)
            return jsonify({"The products is ": products})
        
        except ProductNotFound as error:
            return jsonify({"message": error}), 404
        
        
        
        
        
prod.add_url_rule(
    "/login",
    view_func=ProductView.as_view("ProductView"),
    methods=["GET"])