from models import user
from models.product import Product, products
from models.order import Order
from models.user import User
from models.category import Category, categorys
from flask import Flask, jsonify, request
import sqlite3


app = Flask(__name__)

con = sqlite3.connect("databese.db",check_same_thread=False )
cur = con.cursor()

@app.route('/products')
def getProducts():
    requested_category_id  = request.args.get('category_id')
    if requested_category_id is not None:
        requested_category_id = int(requested_category_id)
        result= cur.execute(f"SELECT * FROM Product WHERE category_id = {requested_category_id }").fetchall()
        products = []
        category = cur.execute(f"SELECT * FROM Category WHERE id = {requested_category_id}").fetchone()
        for prod in result:
            products.append({
                 "id": prod[0],
                 "category": {
                 "id": category[0],
                 "name": category[1]  
                 }, 
                "name": prod[2],
                "price": prod[3],
                "description": prod[4],
                "size": prod[5],
                "color": prod[6],
                "quantity": prod[7]
        })
        return jsonify({"The products are": products })
    else:
        return jsonify({"error"}), 404
    
@app.route('/categorys')
def getCategory():
    cate = cur.execute("SELECT * FROM Category")
    category = cate.fetchall()
    for cat in category:
        categorys.append({
            "id": cat[0],
            "name": cat[1]
        })
    return jsonify({"Categorys": categorys })

@app.route('/createdcategory', methods = ['POST'])
def addCategory():
    data = request.get_json()
    name = data.get('name')
    
    cur.execute('INSERT INTO "Category" (name) VALUES (?)',(name,))
    con.commit()
    
    return jsonify({"mensage": "Category created successfully"})
    
        
    
@app.route('/products/<name_product>')
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


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    required_fields = ['names', 'identification', 'email', 'password', 'registrationData']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400

    identification = data['identification']

    try:
        cur.execute('SELECT * FROM User WHERE identification = ?', (identification,))
        if cur.fetchone():
            return jsonify({"error": "The user is already registered"}), 409
        
        cur.execute('INSERT INTO "User" (names, identification, email, password, registrationData) VALUES (?, ?, ?, ?, ?)', 
                    (data['names'], data['identification'], data['email'], data['password'], data['registrationData']))
        con.commit()
        return jsonify({"message": "User created successfully"}), 201
    except sqlite3.DatabaseError as e:
        con.rollback()
        return jsonify({"error": str(e)}), 500
    
    

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    required_fields = ['email', 'password']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400
        
    email = data['email']
    password = data['password']
    try:
        cur.execute('SELECT * FROM User WHERE email = ? AND password = ?', (email, password))
        userData = cur.fetchone()
        if userData:
            return jsonify({"message": "correct start of session"}),201
            
        return jsonify({"Error": "failed to start"})
            
    except ValueError as ve:
        return jsonify({"The password or email is incorrect": str(ve)}),401
        
        

if  __name__ == '__main__':
    app.run(debug=True, port=5000)