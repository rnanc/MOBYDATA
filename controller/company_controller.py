from flask import request, Blueprint, render_template, url_for, Response, redirect

company_blueprint = Blueprint('company', __name__, template_folder='templates', static_url_path="static")

@company_blueprint.route('/quem_somos', methods=["GET"])
def quem_somos():
    return render_template("quemSomos.html")