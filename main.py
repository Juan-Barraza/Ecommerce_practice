from flask import Flask
from src.routes.routLogin import logi
from src.routes.routproduct import produ
from src.routes.routCategory import cat
from src.routes.routsRegister import regis
from src.database.connectionDb import conection
from src.routes.routCreatCategory import creat
from src.routes.routCreaProd import creatpro
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "token-secret"
jwt = JWTManager(app)

conection.get_connection()

app.register_blueprint(logi)
app.register_blueprint(produ)
app.register_blueprint(cat)
app.register_blueprint(regis)
app.register_blueprint(creat)
app.register_blueprint(creatpro)





if  __name__ == '__main__':
    app.run(debug=True, port=5000)