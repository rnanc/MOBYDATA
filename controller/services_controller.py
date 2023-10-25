from flask import request, Blueprint, render_template, redirect, url_for, Response
from flask_jwt_extended import jwt_required
import services.counter
import services.heat_map
import services.motion_heatmap
from werkzeug.utils import secure_filename
services_blueprint = Blueprint('services', __name__, template_folder='templates', static_url_path="static")

@services_blueprint.route('/video_feed')
@jwt_required
def video_feed():
    video = request.args.get('video')
    video = video if video.isdigit() == False else int(video)
    #Config personalizada na horizontal: largura=50, altura=50, posicao_letra_x=100, posicao_letra_y=50, cor_letra=(0,0,255), sentido_detectar="v", ponto_x_init=5, ponto_x_final=600, ponto_y_init=200, ponto_y_final=200
    return Response(services.counter.Rodar(cam=video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@services_blueprint.route('/heat_map')
@jwt_required
def heat_map():
    video = request.args.get('video')
    video = video if video.isdigit() == False else int(video)
    return Response(services.heat_map.Rodar(cam=video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@services_blueprint.route('/motion_heatmap')
@jwt_required
def motion_heatmap():
    video = request.args.get('video')
    video = video if video.isdigit() == False else int(video)
    return Response(services.motion_heatmap.Rodar(cam=video),
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

@services_blueprint.route('/video_report', methods=["GET", "POST"])
@jwt_required
def video_report():
    if request.method == "POST":
        username = request.cookies.get('username')
        f = request.files['file']
        name_file = f.filename
        f.save("static/video/" + secure_filename(name_file))
        renderizar = request.form["cam"]
        video="static/video/"+name_file
        return render_template("RelatorioDeVideo.html", username=username, renderizar=renderizar, video=video)
    else:
        username = request.cookies.get('username')
        video=0
        return render_template("RelatorioDeVideo.html", username=username, video=video)
