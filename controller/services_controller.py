from flask import request, Blueprint, render_template, redirect, url_for, Response
from flask_jwt_extended import jwt_required
import services.counter
import services.heat_map
import services.motion_heatmap
services_blueprint = Blueprint('services', __name__, template_folder='templates', static_url_path="static")

@services_blueprint.route('/video_feed')
@jwt_required
def video_feed():
    return Response(services.counter.Rodar("static/video/CESUPA.mp4"),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@services_blueprint.route('/heat_map')
@jwt_required
def heat_map():
    return Response(services.heat_map.Rodar("static/video/teste2.mp4"),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@services_blueprint.route('/motion_heatmap')
@jwt_required
def motion_heatmap():
    return Response(services.motion_heatmap.Rodar('static/video/supermarket.mp4'),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@services_blueprint.route('/golive', methods=["GET", "POST"])
@jwt_required
def golive():
    if request.method == "POST":
        username = request.cookies.get('username')
        renderizar = request.form["cam"]
        return render_template("goLive.html", username=username, renderizar=renderizar)
    else:
        username = request.cookies.get('username')
        return render_template("goLive.html", username=username)
