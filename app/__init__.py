from flask import Flask, redirect, url_for
from config.database.environment_variable import POSTGRES_USER, POSTGRES_PW, POSTGRES_DB, POSTGRES_URL
from config.database.model import configure as db_config
from config.database.serealizer import configure as ma_config
from flask_migrate import Migrate
from controller.home_controller import home_blueprint
from controller.report_controller import report_blueprint
from controller.user_controller import user_blueprint
from flask_jwt_extended import JWTManager, set_access_cookies

app = Flask(__name__)
DB_URL = 'postgresql+psycopg2://{user}:{passw}@{port}/{db}'.format(user=POSTGRES_USER, passw=POSTGRES_PW, port=POSTGRES_URL, db=POSTGRES_DB)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #silence the deprecation warning
app.config['JWT_SECRET_KEY'] = "pastelzinho de mel"
app.config['JWT_TOKEN_LOCATION'] = "cookies"
app.config['JWT_COOKIE_CSRF_PROTECT'] = False

db_config(app)
ma_config(app)
Migrate(app, app.db)
jwt = JWTManager(app)
@jwt.expired_token_loader
@jwt.invalid_token_loader
@jwt.unauthorized_loader
def my_expired_token_callback(expired_token):
    return redirect(url_for("home.home"))
app.register_blueprint(home_blueprint)
app.register_blueprint(report_blueprint)
app.register_blueprint(user_blueprint)
if __name__ == "__main__":
    app.run(debug=True, port=8080)