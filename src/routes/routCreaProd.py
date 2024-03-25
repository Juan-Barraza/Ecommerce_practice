from flask import Blueprint, jsonify, request, views
from flask_jwt_extended import jwt_required
from src.services.createdProd import CreatedProduct

creatpro = Blueprint('createdProduct_blueprint', __name__)

class CreatedProdView(views.MethodView):
    
    @jwt_required()
    def post(self):
        
        try:
            data = request.get_json()
            required_fields = ['category_id', 'name', 'price', 'description', 'size', 'color', 'quantity']
            
            if not all(field in data and data[field] for field in required_fields):
                return jsonify({"error": "Missing fields"}), 400
            
            
            
            created = CreatedProduct.createdProduct(data)
        
            if created is not None:
                return jsonify({"Error": "Product not created"}), 401
            

            return jsonify({"menssage": "successfully created product "}), 201
            
            
        except ValueError as e:
            return jsonify({"Error": str(e)})
        
        
creatpro.add_url_rule(
    '/created_product',
    view_func=CreatedProdView.as_view('CreatedProduct'),
    methods=['POST'])