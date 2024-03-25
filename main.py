from flask import Flask
from src.blueprints.blueprints import mainBlu
from src.database.connectionDb import conection
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "token-secret"
jwt = JWTManager(app)
conection.get_connection()

app.register_blueprint(mainBlu)



if  __name__ == '__main__':
    app.run(debug=True, port=5000)