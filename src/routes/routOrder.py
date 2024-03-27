from flask import Blueprint, jsonify, request, views
from flask_jwt_extended import jwt_required
from src.services.createdOrder import CretedOrder


order = Blueprint('order_blueprint', __name__)


class OrderView(views.MethodView):
    
    @jwt_required()
    def post(self):
        
        try:
            data = request.get_json()
            required_fields = ['id_user', 'total_price', 'created_at', 'product_ids']
                
            if not all(field in data and data[field] for field in required_fields):
                return jsonify({"error": "Missing fields"}), 400
            
            insert = CretedOrder.addOrder(data)
            
            if  insert is not None:
                return jsonify({"Error": "Insert failed to order"}), 400 
            
            created = CretedOrder.createdOrderProd(data)
            
            if created is not None:
                return jsonify({"Error": "Not created Order"}), 401
            
            
            return jsonify({"menssage": "Order inserted successfully"}), 201
        
        except ValueError as e:
            return jsonify({"Error": str(e)}),  400
    


order.add_url_rule(
    "/order",
    view_func=OrderView.as_view("OrderView"),
    methods=["POST"])