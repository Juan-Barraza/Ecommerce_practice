from flask import Blueprint, jsonify, views
from flask_jwt_extended import jwt_required
from src.services.searchProduct import SearchProduct


serch = Blueprint('search_blueprint', __name__)

class SearchProductView(views.MethodView):
    
    @jwt_required()
    def get(self):
        
        try:
            search =SearchProduct.search()
            
            if search is None:
                return jsonify({"mensaage": "Product not found"}), 404
            
            print(search)
            products = []
            if isinstance(search, (list, tuple, dict)) and search:
                for prod in search:
                    productsInfo =({
                    "id": prod[0],
                    "id_category": prod[1],
                    "name": prod[2],
                    "price": prod[3],
                    "description": prod[4],
                    "size": prod[5],
                    "color": prod[6],
                    "quantity": prod[7]
                 })
                    products.append(productsInfo)
                
            return jsonify({"Product": products }), 200
        
        except ValueError as error:
            return jsonify({"Error": error}), 500
    


serch.add_url_rule(
    '/product',
    view_func=SearchProductView.as_view('searchprodView'),
    methods=['GET']) 