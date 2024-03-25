from flask import Blueprint, jsonify, views
from flask_jwt_extended import jwt_required
from src.services.category import Category
from src.utils.exceptions.exception import CategoryNotFound


cat = Blueprint('catego_blueprint', __name__)

class CategorysView(views.MethodView):
    
    @jwt_required()
    def get(self):
        
        try:
            category = Category.getCategory()
            
            if(not category):
                return jsonify({"mensaage": "Category not found"})
            
            if isinstance(category, (list, tuple, dict)) and category:
                categorys = []
                for cat in category:
                    infoCategory = {
                    "id": cat[0],
                    "name": cat[1]
                    }
                    categorys.append(infoCategory)
                
            return jsonify({"Categorys": categorys })
        
        except CategoryNotFound as error:
            return jsonify({"Error": error}), 404
    


cat.add_url_rule(
    '/categorys',
    view_func=CategorysView.as_view('CategorysView'),
    methods=['GET']) 