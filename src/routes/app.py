from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
import sqlite3


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "token-secret"
jwt = JWTManager(app)
con = sqlite3.connect("databese.db",check_same_thread=False )
cur = con.cursor()

    
@app.route('/createdproducts', methods = ['POST'])
@jwt_required()
def addProduct():
    data = request.get_json()
    
    required_fields = ['category_id', 'name', 'price', 'description', 'size', 'color', 'quantity']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400
    
    try:
        cur.execute('INSERT INTO "Product" (category_id, name, price, description, size, color, quantity) VALUES (?,?,?,?,?,?,?)', 
                        (data['category_id'], data['name'], data['price'], data['description'], data['size'], data['color'], data['quantity']))
        con.commit()
        
        return jsonify({"mensasage": "Created product successfully"}), 201

    except Exception as a:
        return jsonify({"Error": str(a)}), 401
    

    
        
    
@app.route('/products/<name_product>')
@jwt_required()
def getProduct(name_product):
    res = cur.execute(f"SELECT * FROM Product WHERE name LIKE '%{name_product}%'")   
    result = res.fetchall()    
    products = []
    for prod in result:
        products.append({
            "id": prod[0],
            "name": prod[1],
            "price": prod[2],
            "description": prod[3],
            "size": prod[4],
            "color": prod[5],
            "quantity": prod[6]
        })
    if products:
        return  jsonify({"The product are": products })
    else:
        return jsonify({"message": "product not faund"}), 404
    

@app.route('/order', methods=['POST'])
@jwt_required()
def addOrder():
    data = request.get_json()
        
    required_fields = ['id_user', 'total_price', 'created_at', 'product_ids']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400
    try:
        
        cur.execute('INSERT INTO "Orders" (user_id, total_price, created_at) VALUES (?,?,?)', 
                        (data['id_user'], data['total_price'], data['created_at']))
        con.commit()

        cur.execute('SELECT * FROM "Orders" ORDER BY id DESC LIMIT 1')
        order = cur.fetchone()
        for prod_id in data['product_ids']:
            cur.execute('INSERT INTO "OrderProduct" (order_id, product_id) VALUES (?,?)', 
                        (order[0], prod_id))
            con.commit()

        cur.execute('SELECT * FROM "OrderProduct" ORDER BY id DESC LIMIT 1')
        order = cur.fetchone()
        
        return jsonify({"message": "Order inserted successfully"}),201
    
    except ValueError as a:
        return jsonify({"Error": str(a)}), 401
        
    except Exception as ve:
        return jsonify({"The Order was not inserted successfully: " ,str(ve)}),500


if  __name__ == '__main__':
    app.run(debug=True, port=5000)