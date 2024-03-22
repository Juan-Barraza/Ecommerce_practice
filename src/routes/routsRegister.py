from flask import Blueprint, jsonify, request, views
from src.services.register import Register
from src.utils.exceptions.exception import  ErrorCreatedUser

regis = Blueprint('register_bluprint', __name__)

class RegisterView(views.MethodView):
         
    def post(self):
        
        try:
            data = request.get_json()
            required_fields = ['names', 'identification', 'email', 'password', 'registrationData']
            
            if not all(field in data for field in required_fields):
                return jsonify({"error": "Missing fields"}), 400
            
            
            check = Register.check()
            if check is not None:
                return jsonify({"menssage": "The user already existing"}), 400
                 
            userCreated = Register.createdUser()

            if userCreated is not None:
                return jsonify({"menssage": "User created successfully"}), 201
        
            
        except ErrorCreatedUser as error:
            return jsonify({"Menssage": str(error)}), 401
        
                         
                
regis.add_url_rule(
    '/register',
    view_func=RegisterView.as_view('Registerview'),
    methods=['POST']
)