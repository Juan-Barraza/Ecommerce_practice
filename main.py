from flask import Flask
from src.routes.routLogin import logi
from src.routes.routproduct import prod
from src.database.connectionDb import conection
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "token-secret"
jwt = JWTManager(app)

conection.get_connection()

app.register_blueprint(logi)
app.register_blueprint(prod)




if  __name__ == '__main__':
    app.run(debug=True, port=5000)