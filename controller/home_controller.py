from flask import request, Blueprint, render_template

home_blueprint = Blueprint('home', __name__, template_folder='templates', static_url_path="static")

@home_blueprint.route('/', methods=["GET"])
def home():
  if not request.cookies.get('logado'):
      return render_template("signIn.html")
  else:
      return render_template("quemSomos.html")

@home_blueprint.route('/quem_somos', methods=["GET"])
def quem_somos():
    return render_template("quemSomos.html")

@home_blueprint.route('/fale_conosco', methods=["GET"])
def fale_conosco():
    return render_template("faleConosco.html")

