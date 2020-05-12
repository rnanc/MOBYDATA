from flask import request, Blueprint, current_app
from config.database.model import Report, Users
from config.database.serealizer import ReportSchema, UserSchema
import json
from flask_jwt_extended import jwt_required
report_blueprint = Blueprint('report', __name__, template_folder='templates')

@report_blueprint.route('/create_report', methods=["POST"])
#@jwt_required
def create_report():
    bs = ReportSchema()
    current_app.db.session.commit()
    report = request.json
    user_query = Users.query.filter(Users.username == report["owner"]).first()
    report.pop("owner", None)
    report = bs.load(report)
    current_app.db.session.add(report)
    user_query.reports.append(report)
    current_app.db.session.commit()
    return bs.jsonify(report), 201

@report_blueprint.route('/read_report', methods=["GET"])
#@jwt_required
def read_report():
    bs = ReportSchema(many=True)
    result = Report.query.all()
    return bs.jsonify(result), 200

@report_blueprint.route('/update_report/<identifier>', methods=["POST"])
@jwt_required
def update_report(identifier):
    bs = ReportSchema(many=True)
    query = Report.query.filter(Report.id == identifier)
    query.update(request.json)
    current_app.db.session.commit()
    result = Report.query.all()
    return bs.jsonify(result), 200

@report_blueprint.route('/delete_report/<identifier>', methods=["GET"])
@jwt_required
def delete_report(identifier):
    bs = ReportSchema(many=True)
    Report.query.filter(Report.id == identifier).delete()
    current_app.db.session.commit()
    result = Report.query.all()
    return bs.jsonify(result), 200



