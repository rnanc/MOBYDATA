Requisitos:

- PostgreSQL
- PgAdmin 4
- Conda
- Virtualenv
- Python 3.7

download Postgre: https://www.postgresql.org/download/

Como instalar: https://www.postgresqltutorial.com/install-postgresql/

Após instalar o Postgre, inicie o PgAdmin 4. Crie uma senha para seu banco e após isso vá na pasta do projeto do MOBYDATA. 

Abra o arquivo `database_config.txt` e insira as seguintes informações nessa ordem:

- localhost

- postgres

- (sua senha do banco de dados)

- postgres (nome do seu banco de dados, por padrão é criado o postgres)

Após a instalação do postgre, instale o Conda.

guia de instalação do conda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

como criar virtualenv no conda: https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html

Após instalar o conda, no momento da criação da virtualenv dentro do projeto MOBYDATA utilize o comando:
 
>conda create --name (nome da env) --file requeriments.txt

Para iniciar a virtualenv com os pacotes já instalados.

Inicie sua virtualenv de acordo como mostra o tutorial no site do conda. 

Após iniciado, crie o banco de dados local com os seguintes comandos:

Comando 1:

> flask db init

Comando 2:

> flask db migrate

Comando 3:

> flask db upgrade

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

Volte na sua virtualenv e agora digite o comando:

> python app.py

Será iniciado o servidor local e você já poderá acessar o projeto.
