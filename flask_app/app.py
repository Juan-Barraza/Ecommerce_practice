from models.product import Product, products
from models.order import Order
from models.user import User
from exeptions.exceptions import *
from flask import Flask, jsonify, request
import sqlite3


app = Flask(__name__)

con = sqlite3.connect("databese.db",check_same_thread=False )
cur = con.cursor()

@app.route('/products')
def getProducts():
    res = cur.execute('SELECT * FROM Product')
    result = res.fetchall()
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
    return jsonify({"The products are": products })

@app.route('/products/<name_product>')
def getProduct(name_product):
    res = cur.execute(f"SELECT * FROM Product WHERE name LIKE '%{name_product}%'")   
    result = res.fetchall()    
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
        return  "product not faund", 404

@app.route('/order', methods=['POST'])
def addOrder():
    data = request.get_json()
    id_user = data.get('id_user')
    total_price = data.get('total_price')
    created_at = data.get('created_at')
    product_ids = data.get('product_ids')
    try:
        
        cur.execute('INSERT INTO "Orders" (user_id, total_price, created_at) VALUES (?,?,?)', 
                        (id_user, total_price, created_at))
        con.commit()

        cur.execute('SELECT * FROM "Orders" ORDER BY id DESC LIMIT 1')
        order = cur.fetchone()
        for prod_id in product_ids:
            cur.execute('INSERT INTO "OrderProduct" (order_id, product_id) VALUES (?,?)', 
                        (order[0], prod_id))
            con.commit()

        cur.execute('SELECT * FROM "OrderProduct" ORDER BY id DESC LIMIT 1')
        order = cur.fetchone()
        print(order)        

        return "Order inserted successfully"
        
    finally: 
        pass
'''
@app.route('/cart')
def getCart():
    return jsonify({"Cart": cart.products })


@app.route('/cart/<name_product>', methods=['DELETE'])
def deleteCart(name_product):
    produc_c = [product for product in cart.products if product['name'] == name_product]
    if (len(produc_c) == 0):
        return jsonify({"mensagge": "product not found"})
    cart.delete(produc_c[0])
    return jsonify({"Delete of product": cart.products })


@app.route('/cart/products', methods=['DELETE'])
def clearCart():
    cart.products.clear()
    return jsonify({"clean cart": cart.products })
'''


if  __name__ == '__main__':
    app.run(debug=True, port=5000)