from flask import Blueprint, jsonify, request, views
from flask_jwt_extended import create_access_token
from src.services.login import Login
from src.utils.exceptions.exception import UserNotExist


logi = Blueprint('log_blueprint', __name__)
                 
class LoginView(views.MethodView):

    def post(self):
        body = request.get_json()
        required_fields = ['email','password']
        

        
        if not all(field in body and body[field] for field in required_fields):
            return jsonify({"error": "Missing or empty fields email and password"}), 400

        
        try:
            user = Login.loginUser()
            if not user:
                return jsonify({"message": "error"}), 400

            access_token = create_access_token(identity=body['email'])
            return jsonify(access_token=access_token), 201
        
        except UserNotExist as error:
            return jsonify({"message": str(error)}), 404


logi.add_url_rule(
    "/login",
    view_func=LoginView.as_view("LoginView"),
    methods=["POST"]
)
