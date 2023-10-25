from flask_marshmallow import Marshmallow, fields
from config.database.model import Report, Users
ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class ReportSchema(ma.ModelSchema):
    class Meta:
        model = Report

class UserSchema(ma.ModelSchema):
    class Meta:
        model = Users