import sqlite3
from flask import request
from src.database.connectionDb import conection


class CreatCategory:
    
    
    @classmethod
    def check(cls):
        con = conection.get_connection()
        data = request.get_json()


        try:
            
            query = 'SELECT * FROM "Category" WHERE name = ?'
            params = (data['name'],)
            comp = conection.execute_query(con, query, params)
            
            return comp
        
            
        
        except sqlite3.Error as e:
            return e
    
    
    @classmethod
    def createdCategory(cls, name):
        con = conection.get_connection()
        
        try:
         
            query = 'INSERT INTO "Category" (name) VALUES (?)'
            params = (name,)
            crea = conection.execute_query(con, query, params)
            
            return crea
            
    
        except sqlite3.Error as e:
            return e