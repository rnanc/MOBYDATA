from flask import Flask
from controller.home_controller import home_blueprint

app = Flask(__name__)

#HOME
app.register_blueprint(home_blueprint)

app.run(debug=True, port=8080)
