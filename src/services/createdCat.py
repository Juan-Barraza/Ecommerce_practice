from flask import request
from src.database.connectionDb import conection
from src.utils.exceptions.exception import ErrorCreatedCategory



class CreatCategory:
    
    
    @classmethod
    def check(cls):
        con = conection.get_connection()
        data = request.get_json()
        name = data.get('name')

        try:
            
            query = 'SELECT * FROM "Category" WHERE name = ?'
            params = (name,)
            comp = conection.execute_query(con, query, params,)
            
            if (name,) == comp:
                return True
            
            return False
        
        except ValueError as e:
            return e
    
    
    @classmethod
    def createdCategory(cls):
        con = conection.get_connection()
        data = request.get_json()
        name = data.get('name')
        try:
         
            query = 'INSERT INTO "Category" (name) VALUES (?)'
            params = (name,)
            created = conection.execute_query(con, query, params)
            
            if not created:
                raise ErrorCreatedCategory(" not created")
            
            return created
            
    
        except ValueError as e:
            return e