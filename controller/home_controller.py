from flask import request, Blueprint

home_blueprint = Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/', methods=["GET", "POST"])
def home():
    if request.method == 'GET':
        if not request.cookies.get('logado'):
            return '''
                    <h2>Bem vindos a Mobility Data!</h2>
                    <form  action="/login_user" method="post">
                        <input name="username" placeholder='Login'/>
                        <input name="password" placeholder='Senha'/> 
                        <input name="provider" value="admin" hidden/> 
                        <input type='submit' value='Entrar'/>
                    </form>      
            '''
        else:
            return '''
                    <h2>Bem vindos a Mobility Data!</h2>
                    <h3>Usuários:</h3>
                    <ul> 
                        <li><a href="/read_user">Acessar todos usuários</a></li>
                        <li><a href="/create_user">Cadastrar usuário</a></li>
                        <li><a href="/update_user/1">Atualizar dados do usuário</a></li>
                        <li><a href="/delete_user">Deletar usuário</a></li>
                        
                    </ul>
                    <h3>Relatórios:</h3>
                    <ul> 
                        <li><a href="/read_report">Acessar todos os relatórios</a></li>
                        <li><a href="/create_user">Gerar relatório</a></li>
                        <li><a href="/read_report">Atualizar dados do relatório</a></li>
                        <li><a href="/create_user">Deletar relatório</a></li>
                    </ul>
            '''


