from models.product import Product, prod
from models.cart import Cart, products
from models.order import Order
from models.user import User
from flask import Flask, jsonify, redirect, request, url_for


app = Flask(__name__)

cart = Cart()

@app.route('/products')
def getProducts():
    return jsonify({"product": prod})

@app.route('/products/<name_product>')
def getname_product(name_product):
    products_found = [product for product in prod if product['name'] == name_product]
    if (len(products_found) > 0):
        return jsonify({"product": products_found[0]})
    return jsonify(["Product not found"])   


@app.route('/products/cart/<name_product>', methods = ['POST'])
def addCart(name_product):
    produc_f = [product for product in prod if product['name'] == name_product]
    if (len(produc_f) == 0):
        return jsonify({"mensagge": "product not found"})
    cart.add(produc_f[0])
    return jsonify({"New Cart": cart.products })


@app.route('/cart')
def getCart():
    return jsonify({"Cart": cart.products })


@app.route('/cart/<name_product>', methods = ['DELETE'])
def deleteCart(name_product):
    produc_c = [product for product in cart.products if product['name'] == name_product]
    if (len(produc_c) == 0):
        return jsonify({"mensagge": "product not found"})
    cart.delete(produc_c[0])
    return jsonify({"Delete of product": cart.products })


@app.route('/cart/products', methods = ['DELETE'])
def clearCart():
    cart.products.clear()
    return jsonify({"clean cart": cart.products })


if  __name__ == '__main__':
    app.run(debug=True, port=5000)