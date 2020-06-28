from flask import redirect, url_for, make_response
from flask_jwt_extended import JWTManager

jwt = JWTManager()

def configure(app):
    jwt.init_app(app)
    @jwt.expired_token_loader
    @jwt.invalid_token_loader
    @jwt.unauthorized_loader
    def my_expired_token_callback(expired_token):
        resp = make_response(redirect(url_for("home.home")))
        resp.set_cookie('access_token_cookie', "")
        resp.set_cookie('username', "")
        return resp