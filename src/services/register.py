from flask import request
from src.database.connectionDb import conection

class Register:
    
    @classmethod
    def check(cls):
        con = conection.get_connection()
        data = request.get_json()
        try:

            query = 'SELECT * FROM "User" WHERE identification = ?'
            params = (data['identification'],)
            check = conection.execute_query(con, query, params)
            
            return check
        
        except Exception as e:
            return e
    
    @classmethod
    def createdUser(cls, data):
        con = conection.get_connection()

        
        try:
            
            query = 'INSERT INTO "User" (names, identification, email, password, registrationData) VALUES (?, ?, ?, ?, ?)'
            params = (data['names'], data['identification'], data['email'], data['password'], data['registrationData'])
            userCreated = conection.execute_query(con, query, params)

            return userCreated
            
        except Exception as e:
            return e