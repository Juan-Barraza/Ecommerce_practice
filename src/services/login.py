from flask import request
from src.database.connectionDb import conection
from src.utils.exceptions.exception import UserNotExist


class Login:
    
    @classmethod
    def loginUser(cls):
        con = conection.get_connection()
        body = request.get_json()

        try:
            query = 'SELECT * FROM User WHERE email = ? AND password = ?'
            params = (body["email"], body["password"])
            userData = conection.execute_query(con, query, params)
            
            if not userData:
                raise UserNotExist("Usuario no existe") 
            
            return userData
            
        except ValueError as ve:
            return ve

        
            