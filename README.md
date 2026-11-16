🥖 Padaria.sys — Sistema de Gerenciamento de Padaria

Sobre o projeto

O Padaria.sys é um sistema de gerenciamento de padaria desenvolvido como parte do Projeto Integrado das disciplinas de Desenvolvimento Web (DWS), Programação Orientada a Objetos (POO) e Banco de Dados (BD).

O objetivo é desenvolver uma aplicação que facilite o gerenciamento de uma padaria, permitindo o cadastro e a consulta de clientes, funcionários e produtos, além do registro e acompanhamento de pedidos.

Tecnologias utilizadas

HTML5: estrutura das páginas do sistema.

CSS3: estilização e design da interface.

JavaScript: interatividade e comunicação com a API.

Python: desenvolvimento do back-end.

Flask: criação das rotas da API.

MySQL: armazenamento dos dados.

XAMPP: gerenciamento do servidor MySQL e acesso ao phpMyAdmin.

mysql-connector-python: conexão entre Python e MySQL.

Estrutura de pastas

Padaria_do_dudu/
│
├── index.html
├── README.md
│
├── backend/
│   ├── app.py
│   ├── conexao.py
│   ├── testar_conexao.py
│   ├── requirements.txt
│   │
│   ├── daos/
│   │   ├── __init__.py
│   │   └── dao.py
│   │
│   └── models/
│       ├── __init__.py
│       └── entidades.py
│
├── database/
│   └── banco_padaria.sql
│
├── diagrama_de_classes/
│   ├── conceitual.PNG
│   └── logico.PNG
│
├── pages/
│   ├── clientes.html
│   ├── funcionarios.html
│   ├── pedidos.html
│   └── produtos.html
│
├── script/
│   └── script.js
│
└── style/
    └── style.css

Banco de dados

O banco de dados utilizado no projeto se chama sistema_padaria.

O arquivo responsável por sua criação é:

database/banco_padaria.sql

O banco possui cinco tabelas principais:

Tabela

Descrição

clientes

Armazena os dados dos clientes.

funcionarios

Armazena os dados dos funcionários.

produtos

Armazena os produtos disponíveis na padaria.

pedidos

Registra os pedidos realizados.

itens_pedido

Armazena os produtos e as quantidades de cada pedido.

As tabelas utilizam chaves primárias e estrangeiras para organizar os relacionamentos entre os dados.

Como instalar e executar o projeto

1. Instalar o XAMPP

Baixe o XAMPP pelo site oficial:

https://www.apachefriends.org/pt_br/index.html

Após a instalação:

Abra o XAMPP Control Panel.

Inicie o serviço Apache.

Inicie o serviço MySQL.

2. Importar o banco de dados

Abra o navegador e acesse http://localhost/phpmyadmin.

Entre na aba Importar.

Clique em Escolher arquivo.

Selecione database/banco_padaria.sql.

Clique em Importar ou Executar.

Verifique se o banco sistema_padaria foi criado.

O arquivo SQL já contém os comandos para criar e selecionar o banco de dados, portanto não é necessário criá-lo manualmente antes da importação.

3. Configurar a conexão com o banco

O arquivo responsável pela conexão é:

backend/conexao.py

As configurações utilizadas são:

Host: localhost

Usuário: root

Senha: vazia, na instalação padrão do XAMPP.

Banco de dados: sistema_padaria

Porta: 3306

Caso tenha configurado uma senha ou outra porta no MySQL, atualize as informações no arquivo de conexão.

4. Instalar as dependências

Abra o terminal do VS Code na pasta principal do projeto e execute:

cd backend
pip install -r requirements.txt

5. Testar a conexão

Ainda dentro da pasta backend, execute:

python testar_conexao.py

Esse arquivo permite verificar se o Python está conseguindo se conectar ao banco de dados.

6. Iniciar o servidor Flask

Na pasta backend, execute:

python app.py

O servidor será iniciado no endereço:

http://127.0.0.1:5000

Mantenha o terminal aberto enquanto estiver utilizando o sistema.

7. Abrir o site

Coloque a pasta Padaria_do_dudu dentro do diretório:

C:\xampp\htdocs\

Com o Apache iniciado, acesse:

http://localhost/Padaria_do_dudu/

O arquivo index.html será a página inicial do sistema.

Rotas da API

A API utiliza o endereço base:

http://127.0.0.1:5000

Método

Rota

Funcionalidade

GET

/

Apresenta informações da API.

GET

/api/clientes

Consulta os clientes.

POST

/api/clientes

Cadastra clientes.

GET

/api/funcionarios

Consulta os funcionários.

POST

/api/funcionarios

Cadastra funcionários.

GET

/api/produtos

Consulta os produtos.

POST

/api/produtos

Cadastra produtos.

GET

/api/pedidos

Consulta os pedidos.

POST

/api/pedidos

Registra pedidos e seus itens.

Organização dos arquivos

index.html: página inicial do sistema.

backend/app.py: aplicação Flask e rotas da API.

backend/conexao.py: conexão com o banco de dados.

backend/testar_conexao.py: teste de conexão com o MySQL.

backend/daos/dao.py: operações de acesso ao banco de dados.

backend/models/entidades.py: classes que representam as entidades do sistema.

backend/requirements.txt: dependências necessárias para executar o back-end.

database/banco_padaria.sql: criação do banco, tabelas e dados iniciais.

diagrama_de_classes/: diagramas conceitual e lógico.

pages/: páginas de gerenciamento de clientes, funcionários, produtos e pedidos.

script/script.js: funcionalidades e comunicação com a API.

style/style.css: estilos visuais do sistema.

Observações

O XAMPP deve estar com o MySQL iniciado para que o sistema consiga acessar o banco.

O servidor Flask também precisa estar em execução para que as funcionalidades que utilizam a API funcionem.

O endereço da API utilizado pelo JavaScript é http://127.0.0.1:5000.

A configuração de CORS deve permitir a comunicação entre o front-end e o Flask quando forem executados em origens diferentes.

Informações acadêmicas

Instituição: Colégio UNASP-HT
Projeto: Sistema de Gerenciamento de Padaria
Disciplinas: DWS, POO e Banco de Dados
Turma: 2° TIA
Ano: 2026
