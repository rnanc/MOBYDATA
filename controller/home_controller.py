from flask import request, Blueprint, render_template, url_for, Response
from flask_jwt_extended import  jwt_required
from config.database.serealizer import UserSchema, ReportSchema
from config.database.model import Users, Report
import services.counter
home_blueprint = Blueprint('home', __name__, template_folder='templates', static_url_path="static")

@home_blueprint.route('/video_feed')
def video_feed():
        return Response(services.counter.Rodar("static/video/CESUPA.mp4"),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@home_blueprint.route('/', methods=["GET"])
def home():
    return render_template("signIn.html")

@home_blueprint.route('/logado', methods=["GET"])
@jwt_required
def logado():
    username = request.cookies.get('username')
    return render_template("dashboard.html", username=username)

@home_blueprint.route('/golive', methods=["GET"])
@jwt_required
def golive():
    username = request.cookies.get('username')
    return render_template("goLive.html", username=username)

@home_blueprint.route('/relatorio', methods=["POST"])
@jwt_required
def relatorio():
    rs = ReportSchema()
    form = request.form.to_dict()
    form["date"] = form["date"].replace("-", "/")
    username = request.cookies.get('username')
    report_query = Report.query.filter_by(report_type=form["TYPE"], date = form["date"]).first()
    return render_template("relatorio.html", username=username, report_image=report_query.image, report_date=report_query.date)

@home_blueprint.route('/quem_somos', methods=["GET"])
def quem_somos():
    return render_template("quemSomos.html")



