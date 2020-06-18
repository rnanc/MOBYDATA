from flask import request, Blueprint, render_template, url_for, redirect
from flask_jwt_extended import jwt_required, get_jwt_identity, jwt_optional

home_blueprint = Blueprint('home', __name__, template_folder='templates', static_url_path="static")

@home_blueprint.route('/', methods=["GET"])
@jwt_optional
def home():
    current_user = get_jwt_identity()
    if current_user:
        return redirect(url_for("home.logado"))
    else:
        return render_template("signIn.html")

@home_blueprint.route('/logado', methods=["GET"])
@jwt_required
def logado():
    username = request.cookies.get('username')
    return render_template("dashboard.html", username=username)