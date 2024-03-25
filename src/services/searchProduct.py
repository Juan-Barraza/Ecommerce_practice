from flask import request
from src.database.connectionDb import conection


class SearchProduct:
    
    @classmethod
    def search(cls):
        con = conection.get_connection()
        requested_name  = request.args.get('name_product')

        try:
            
            query = 'SELECT * FROM "Product" WHERE name LIKE ? '
            if requested_name is None:
                return None
            params = ('%' + requested_name + '%',)
            search = conection.execute_query(con,query,params,fetch_all=True)
            
            return search
        
        except KeyError as a:
            return a