from flask import Blueprint, jsonify, views
from flask_jwt_extended import jwt_required
from src.services.product import Product
from src.utils.exceptions.exception import CategoryNotFound, ProductNotFound

produ = Blueprint('produc_blueprint', __name__)


class ProductsView(views.MethodView):
    
    @jwt_required()
    def get(self):
        
        try:
            products = Product.getProducts()

            if not products:
                return jsonify({"message": "Product not found" })
            
                             
            category = Product.getCategoryPro()
            if not category:
                return jsonify({"message": "Category not found" })
            
            infoCategory = {
                "id": category[0] if (category and isinstance(category, (list, tuple))) else None,
                "name": category[1] if (category and isinstance(category, (list, tuple))) else None
            }
            
            products_list = []
            for prod in products:
                
                if isinstance(prod, (list, tuple)):
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
                    products_list.append(product_info)
                else:
                    pass

            return jsonify({"The products are": products_list})
        
        except CategoryNotFound as error:
            return jsonify({"message": error}), 404
        
        except ProductNotFound as error:
            return jsonify({"message": error}), 404
        
        except ValueError as e:
            return jsonify({"Error": str(e)})
        
        
        
        
produ.add_url_rule(
    "/products",
    view_func=ProductsView.as_view("ProductsView"),
    methods=["GET"])