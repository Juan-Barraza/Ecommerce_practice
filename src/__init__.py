from flask import Blueprint
from src.routes.routLogin import logi
from src.routes.routproduct import produ
from src.routes.routCategory import cat
from src.routes.routsRegister import regis
from src.routes.routCreatCategory import creat
from src.routes.routCreaProd import creatpro
from src.routes.routSerchPro import serch
from src.routes.routOrder import order

mainBlu = Blueprint('main', __name__)

mainBlu.register_blueprint(logi)
mainBlu.register_blueprint(produ)
mainBlu.register_blueprint(cat)
mainBlu.register_blueprint(regis)
mainBlu.register_blueprint(creat)
mainBlu.register_blueprint(creatpro)
mainBlu.register_blueprint(serch)
mainBlu.register_blueprint(order)