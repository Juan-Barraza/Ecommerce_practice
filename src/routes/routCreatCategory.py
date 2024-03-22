from flask import Blueprint, jsonify, request, views
from flask_jwt_extended import jwt_required
from src.services.createdCat import CreatCategory
from src.utils.exceptions.exception import ErrorCreatedCategory

creat = Blueprint('created_cat_blueprint', __name__)

class CreatedCatView(views.MethodView):
    
    @jwt_required()
    def post(self):
        
        try:
            data = request.get_json()
            required_fields = ['name']
            
            if not all(field in data for field in required_fields):
                return jsonify({"error": "Missing fields"}), 400
            
            exist = CreatCategory.check()
            
            if exist:
                return jsonify({"mensage":"Category already exists"}), 409
            
            
            created = CreatCategory.createdCategory()
            
            if not created:
                return jsonify({"Error": "Create category failed"}), 401
            

            return jsonify({"mensage": "Category created successfully"}), 201
            
            
        except ErrorCreatedCategory as error:
            return jsonify({"mensage": str(error)})
        
        except ValueError as e:
            return jsonify({"Error": str(e)})
        
        
creat.add_url_rule(
    '/created_category',
    view_func=CreatedCatView.as_view('CreatedcatView'),
    methods=['POST'])