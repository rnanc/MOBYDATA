from flask import redirect, url_for
from flask_jwt_extended import JWTManager

jwt = JWTManager()

def configure(app):
    jwt.init_app(app)
    @jwt.expired_token_loader
    @jwt.invalid_token_loader
    @jwt.unauthorized_loader
    def my_expired_token_callback(expired_token):
        return redirect(url_for("home.home"))