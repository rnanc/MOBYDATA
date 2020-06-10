from flask import request, Blueprint, render_template
from flask_jwt_extended import  jwt_required
home_blueprint = Blueprint('home', __name__, template_folder='templates', static_url_path="static")

@home_blueprint.route('/', methods=["GET"])
def home():
    return render_template("signIn.html")

@home_blueprint.route('/logado', methods=["GET"])
@jwt_required
def logado():
    return render_template("dashboard.html")

@home_blueprint.route('/quem_somos', methods=["GET"])
def quem_somos():
    return render_template("quemSomos.html")



