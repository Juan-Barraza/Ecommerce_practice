from flask import Blueprint, jsonify, request, views
from flask_jwt_extended import jwt_required
from src.services.createdCat import CreatCategory

creat = Blueprint('created_cat_blueprint', __name__)

class CreatedCatView(views.MethodView):
    
    @jwt_required()
    def post(self):
        
        try:
            data = request.get_json()
            name = ['name']
            
            if not all(field in data and data[field] for field in name):
                return jsonify({"error": "Missing fields"}), 400
            
            exist = CreatCategory.check()
            if exist is not None:
                return jsonify({"mensage":"Category already exists"}), 409
            
            
            created = CreatCategory.createdCategory(data['name'])
            if created is not None:
                return jsonify({"Error": "Category not created"}), 401
            

            return jsonify({"mensage": "successfully created category "}), 201
            
            
        except ValueError as e:
            return jsonify({"Error": str(e)})
        
        
creat.add_url_rule(
    '/created_category',
    view_func=CreatedCatView.as_view('CreatedcatView'),
    methods=['POST'])