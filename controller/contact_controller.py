from flask import request, Blueprint, render_template, redirect, url_for
from config.mail.mail import send_message
contact_blueprint = Blueprint('contact', __name__, template_folder='templates', static_url_path="static")

@contact_blueprint.route('/fale_conosco', methods=["GET", "POST"])
def fale_conosco():
    if request.method == "POST":
        subject = request.form["subject"]
        email = request.form["email"]
        body = request.form["body"]
        send_message(subject, email, body)
        return redirect(url_for("home.home"))
    else:
        return render_template("faleConosco.html")