from flask import render_template, request, Blueprint

home_blueprint = Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/', methods=["GET"])
def home():
    return '''
            <h1>Olá mundo!</h1>
            <h2>Bem vindos a Mobility Data!</h2>
            <input placeholder='Login'/>
            <input placeholder='Senha'/> 
            <input type='submit' value='Entrar'/>         
    '''