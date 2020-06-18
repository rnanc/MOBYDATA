from flask import request, Blueprint, render_template, url_for, Response
from flask_jwt_extended import  jwt_required
from config.database.serealizer import UserSchema, ReportSchema
from config.database.model import Users, Report
import services.counter
import services.heat_map
import services.motion_heatmap
home_blueprint = Blueprint('home', __name__, template_folder='templates', static_url_path="static")

@home_blueprint.route('/video_feed')
def video_feed():
        return Response(services.counter.Rodar("static/video/CESUPA.mp4"),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@home_blueprint.route('/heat_map')
def heat_map():
        return Response(services.heat_map.Rodar(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@home_blueprint.route('/motion_heatmap')
def motion_heatmap():
        return Response(services.motion_heatmap.Rodar(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@home_blueprint.route('/', methods=["GET"])
def home():
    return render_template("signIn.html")

@home_blueprint.route('/logado', methods=["GET"])
@jwt_required
def logado():
    username = request.cookies.get('username')
    return render_template("dashboard.html", username=username)

@home_blueprint.route('/golive', methods=["GET", "POST"])
@jwt_required
def golive():
    if request.method == "POST":
        username = request.cookies.get('username')
        renderizar = request.form["cam"]
        return render_template("goLive.html", username=username, renderizar=renderizar)
    else:
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
    if report_query:
        report_image = report_query.image
        report_date = report_query.date
    else:
        report_image = "None"
        report_date = form["date"]
    return render_template("relatorio.html", username=username, report_image=report_image, report_date=report_date)

@home_blueprint.route('/quem_somos', methods=["GET"])
def quem_somos():
    return render_template("quemSomos.html")



