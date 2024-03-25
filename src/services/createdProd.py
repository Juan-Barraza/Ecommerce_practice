from src.database.connectionDb import conection


class CreatedProduct:
    
    @classmethod
    def createdProduct(cls, data):
        con = conection.get_connection()
        
        try:
            query = 'INSERT INTO "Product" (category_id, name, price, description, size, color, quantity) VALUES (?,?,?,?,?,?,?)'
            params = (data['category_id'], data['name'], data['price'], data['description'], data['size'], data['color'], data['quantity'])
            created = conection.execute_query(con, query, params)
            print(created)
            return created

        except Exception as a:
            return a
    