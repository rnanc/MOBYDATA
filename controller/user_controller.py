from flask import request, Blueprint, current_app, redirect, url_for, make_response
from config.database.serealizer import UserSchema, ReportSchema
from config.database.model import Users, Report
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, set_access_cookies

user_blueprint = Blueprint('user', __name__, template_folder='templates')

@user_blueprint.route('/create_user', methods=["GET","POST"])
#@jwt_required
def register_user():
    if request.method == "POST":
        us = UserSchema()
        user = us.load(request.form.to_dict())
        user.gen_hash()
        current_app.db.session.add(user)
        current_app.db.session.commit()
        return us.jsonify(user), 201
    else:
        return '''
                    <h2>Cadastro de usuário</h2>
                    <form  action="/create_user" method="post">
                        <input name="username" placeholder='Username'/>
                        <input name="email" placeholder='E-mail'/>
                        <input name="password" placeholder='Password'/> 
                        <input name="provider" value="" placeholder='Provider'/> 
                        <input type='submit' value='Cadastrar'/>
                    </form>      
            '''

@user_blueprint.route('/read_user', methods=["GET"])
#@jwt_required
def read_user():
    us = UserSchema(many=True)
    result = Users.query.all()
    return us.jsonify(result), 200

@user_blueprint.route('/update_user/<identifier>', methods=["POST", "GET"])
@jwt_required
def update_user(identifier):
    if request.method == "POST":
        us = UserSchema()
        user_request = request.form.to_dict()
        user = us.load(user_request)
        user.gen_hash()
        user_request["password"] = user.password
        query = Users.query.filter(Users.id == identifier)
        query.update(user_request)
        current_app.db.session.commit()
        us = UserSchema(many=True)
        result = Users.query.all()
        return us.jsonify(result), 200
    else:
        return '''
            <h2>Atualizar dados do usuário</h2>
            <form  action="/update_user/{}" method="post">
                <input name="username" placeholder='Username'/>
                <input name="email" placeholder='E-mail'/>
                <input name="password" placeholder='Password'/> 
                <input name="provider" value="" placeholder='Provider'/> 
                <input type='submit' value='Atualizar'/>
            </form>      
        '''.format(identifier)

@user_blueprint.route('/delete_user/<identifier>', methods=["GET"])
@jwt_required
def delete_user(identifier):
    us = UserSchema(many=True)
    Users.query.filter(Users.id == identifier).delete()
    current_app.db.session.commit()
    result = Users.query.all()
    return us.jsonify(result), 200

@user_blueprint.route('/findone_user/<identifier>', methods=["GET"])
#@jwt_required
def findone_user(identifier):
    us = UserSchema(many=True)
    user = Users.query.filter(Users.username == identifier)
    return us.jsonify(user), 200

@user_blueprint.route('/login_user', methods=["POST"])
def login_user():
    user = request.form.to_dict()
    user_query = Users.query.filter_by(username=user["username"]).first()
    if user_query and user_query.verify_password(user['password']):
        acess_token = create_access_token(identity=user_query.id)
        refresh_token = create_refresh_token(identity=user_query.id)
        response = make_response(redirect(url_for("home.home")))
        response.set_cookie('logado', 'yes')
        response.set_cookie('access_token_cookie', acess_token)
        return response
    return "Usuário ou senha inválidos!", 401