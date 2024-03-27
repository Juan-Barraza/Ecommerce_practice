from src.database.connectionDb import conection



class CretedOrder:
    
    @classmethod
    def addOrder(cls, data):
        con = conection.get_connection()
        
        try:
            query = 'INSERT INTO "Orders" (user_id, total_price, created_at) VALUES (?,?,?)'
            params = (data['id_user'], data['total_price'], data['created_at'])
            result = conection.execute_query(con, query, params)
            
            return result
        
        except ValueError as e:
            return e
        
    
    @classmethod
    def createdOrderProd(cls, data):
        con = conection.get_connection()
        
        try: 
            query = 'SELECT * FROM "Orders" ORDER BY id DESC LIMIT 1'
            result = conection.execute_query(con, query)
            
            crea = [] 
            if data.get('product_ids'):
                for prod_id in data['product_ids']:
                    query2 = 'INSERT INTO "OrderProduct" (order_id, product_id) VALUES (?,?)'
                    params = (result[0], prod_id)
                    crea.append(conection.execute_query(con, query2, params))
            
            return crea
        
        except ValueError as e:
            return e
