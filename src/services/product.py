from flask import request
from src.database.connectionDb import conection
from src.utils.exceptions.exception import ProductNotFound, CategoryNotFound


class Product:
    
    @classmethod
    def getProducts(cls):
        requested_category_id  = request.args.get('category_id')
        con = conection.get_connection()
        
        try:
            if requested_category_id is not None:
                requested_category_id = int(requested_category_id)
                query = 'SELECT * FROM Product WHERE category_id = ?'
                params = (requested_category_id,)
                products_data = conection.execute_query(con, query, params, fetch_all=True)
                
                if not products_data:
                    raise ProductNotFound("Products not found for the given category_id")
                
            else:
                raise ProductNotFound("Product not found")
        except ValueError as e:
            return e
    
    
    
    @classmethod
    def getCategoryPro(cls):
        requested_category_id  = request.args.get('category_id')
        con = conection.get_connection()
        try:
            query = 'SELECT * FROM Category WHERE id = ?'
            param = (requested_category_id)
            category_data = conection.execute_query(con, query, param, fetch_all=False)
                
            if not category_data:
                raise CategoryNotFound("Category not found")
        
        except ValueError as a:
            return a