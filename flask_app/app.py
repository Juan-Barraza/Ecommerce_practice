from models.product import Product
from models.cart import Cart
from models.order import Order
from models.user import User
from flask import Flask


app = Flask(__name__)

@app.route('/admin')
def admin():
    return "Hello world!"












if  __name__ == '__main__':
    app.run(debug=True, port=5000)