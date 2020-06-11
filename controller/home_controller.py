from flask import request, Blueprint, render_template
from flask_jwt_extended import  jwt_required
from config.database.serealizer import UserSchema, ReportSchema
from config.database.model import Users, Report
home_blueprint = Blueprint('home', __name__, template_folder='templates', static_url_path="static")

@home_blueprint.route('/', methods=["GET"])
def home():
    return render_template("signIn.html")

@home_blueprint.route('/logado', methods=["GET"])
@jwt_required
def logado():
    username = request.cookies.get('username')
    return render_template("dashboard.html", username=username)

@home_blueprint.route('/relatorio', methods=["GET"])
@jwt_required
def relatorio():
    username = request.cookies.get('username')
    return render_template("relatorio.html", username=username)

@home_blueprint.route('/quem_somos', methods=["GET"])
def quem_somos():
    return render_template("quemSomos.html")



