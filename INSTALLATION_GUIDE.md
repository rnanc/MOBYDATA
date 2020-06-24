# CLONE OU DOWNLOAD
Faça o download do projeto como .zip ou clone em uma pasta de sua preferência.

# REQUISITOS

- PostgreSQL
- PgAdmin 4
- Conda
- Virtualenv
- Python 3.7

# POSTGRE
download Postgre: https://www.postgresql.org/download/

Como instalar: https://www.postgresqltutorial.com/install-postgresql/

Após instalar o Postgre, inicie o PgAdmin 4. Crie uma senha para seu banco e após isso vá na pasta do projeto do MOBYDATA. 

Abra o arquivo `database_config.txt` e insira as seguintes informações nessa ordem:

- localhost

- postgres

- (sua senha do banco de dados)

- postgres (nome do seu banco de dados, por padrão é criado o postgres)



# CONDA

Após a instalação do postgre, instale o Conda (Anaconda).

guia de instalação do conda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

após instalar o conda, siga os seguintes passos:

- abra seu terminal 
- vá até a pasta do projeto do mobydata
- dentro da pasta, utilize o comando abaixo:

obs: substitua o campo (nome da env) pelo nome que deseja dar para sua virtualenv, como por exemplo: venv
 
>conda create --name (nome da env) --file requeriments.txt

Inicie sua virtualenv usando o comando abaixo de acordo com seu sistema operacional:

No Windows:
>  activate snowflakes

Em macOS e Linux:

>  source activate snowflakes


# CRIANDO BANCO DE DADOS

Após iniciado, crie o banco de dados local com os seguintes comandos:

Comando 1:

> flask db init

Comando 2:

> flask db migrate

Comando 3:

> flask db upgrade

# CRIANDO PRIMEIRO USUÁRIO

Com o banco criado, inicie o seu pgAdmin 4, será aberto uma aba no seu navegador padrão e então você poderá visualizar as informações contidas no banco criado por lá.

No banco, você deve criar seu primeiro usuário para ter acesso ao projeto, então clique em `Servers`->`PostgresSQL 12`->`Databases`->`postgres`

Com o postgres selecionado, no menu superior clique na opção `Tools`->`Query Tool`

Após isso clique em `Query Editor`

E digite o comando:

> select * from users

e aperte `F5`.

Aparecerá uma tabela com as informações do seu banco embaixo. Nos campos 
`id` digite 1, em `username` seu nome de usuário, em `password` sua senha, em `email` seu e-mail e em `company_name` o nome de sua empresa.

Após criar um usuário aperte `F6` para salvar as informações e então você já poderá logar no sistema.

# INICIANDO PROJETO

Volte na sua virtualenv e agora digite o comando:

> python app.py

Será iniciado o servidor local e você já poderá acessar o projeto.
