from src.database.connectionDb import conection
from src.utils.exceptions.exception import CategoryNotFound

class Category:
    
    @classmethod
    def getCategory(cls):
        con = conection.get_connection()
        
        try:
            query = 'SELECT * FROM Category'
            categ = conection.execute_query(con, query, fetch_all=True)
            
            if not categ:
                raise CategoryNotFound("Category not found")
            
            return categ
        
        except CategoryNotFound as e:
            raise CategoryNotFound("Category does not exist")