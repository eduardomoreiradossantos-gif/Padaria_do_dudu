🥖 Padaria.sys

Sistema de Gerenciamento de Padaria

<p align="center">
  <img src="https://img.shields.io/badge/Projeto-Integrado-8B4513?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-Flask-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Database-MySQL-orange?style=for-the-badge&logo=mysql" />
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-green?style=for-the-badge" />
</p>

📌 Sobre o projeto

O Padaria.sys é um sistema de gerenciamento de padaria desenvolvido como parte do Projeto Integrado das disciplinas de Desenvolvimento Web (DWS), Programação Orientada a Objetos (POO) e Banco de Dados (BD).

O objetivo é facilitar a administração de uma padaria, permitindo o cadastro e a consulta de clientes, funcionários e produtos, além do registro e acompanhamento de pedidos.

🚀 Tecnologias utilizadas

Tecnologia

Utilização

🌐 HTML5

Estrutura das páginas

🎨 CSS3

Estilização e design da interface

⚡ JavaScript

Interatividade e comunicação com a API

🐍 Python

Desenvolvimento do back-end

🔥 Flask

Criação das rotas da API

🗄️ MySQL

Armazenamento dos dados

🖥️ XAMPP

Gerenciamento do MySQL e phpMyAdmin

📂 Estrutura do projeto

📁 Padaria_do_dudu/
│
├── 📄 index.html
├── 📄 README.md
│
├── 📁 backend/
│   ├── 📄 app.py
│   ├── 📄 conexao.py
│   ├── 📄 testar_conexao.py
│   ├── 📄 requirements.txt
│   │
│   ├── 📁 daos/
│   │   ├── 📄 __init__.py
│   │   └── 📄 dao.py
│   │
│   └── 📁 models/
│       ├── 📄 __init__.py
│       └── 📄 entidades.py
│
├── 📁 database/
│   └── 📄 banco_padaria.sql
│
├── 📁 diagrama_de_classes/
│   ├── 🖼️ conceitual.PNG
│   └── 🖼️ logico.PNG
│
├── 📁 pages/
│   ├── 📄 clientes.html
│   ├── 📄 funcionarios.html
│   ├── 📄 pedidos.html
│   └── 📄 produtos.html
│
├── 📁 script/
│   └── 📄 script.js
│
└── 📁 style/
    └── 📄 style.css

🗄️ Banco de dados

O projeto utiliza o banco de dados sistema_padaria, criado através do arquivo:

📄 database/banco_padaria.sql

📋 Tabelas do banco

Tabela

Descrição

👥 clientes

Armazena os dados dos clientes.

👨‍🍳 funcionarios

Armazena os dados dos funcionários.

🥐 produtos

Armazena os produtos da padaria.

🛒 pedidos

Registra os pedidos realizados.

📦 itens_pedido

Armazena os produtos e quantidades de cada pedido.

As tabelas utilizam chaves primárias (PK) e chaves estrangeiras (FK) para organizar os relacionamentos entre os dados.

⚙️ Instalação e execução

1️⃣ Instalar o XAMPP

Baixe o XAMPP pelo site oficial:

🔗 https://www.apachefriends.org/pt_br/index.html

Após instalar:

Abra o XAMPP Control Panel.

Inicie o Apache.

Inicie o MySQL.

2️⃣ Importar o banco de dados

Acesse http://localhost/phpmyadmin.

Clique na aba Importar.

Selecione o arquivo database/banco_padaria.sql.

Clique em Importar ou Executar.

Confira se o banco sistema_padaria foi criado.

💡 O arquivo SQL já possui os comandos para criar e selecionar o banco. Não é necessário criá-lo manualmente antes da importação.

3️⃣ Configurar a conexão

O arquivo responsável pela conexão é:

📄 backend/conexao.py

Configurações utilizadas:

Configuração

Valor

Host

localhost

Usuário

root

Senha

Vazia (padrão do XAMPP)

Banco

sistema_padaria

Porta

3306

Caso tenha configurado uma senha diferente no MySQL, atualize o arquivo de conexão.

4️⃣ Instalar as dependências

Abra o terminal na pasta principal do projeto e execute:

cd backend
pip install -r requirements.txt

5️⃣ Testar a conexão com o banco

Execute o comando:

python testar_conexao.py

Esse arquivo verifica se o Python consegue acessar o banco de dados.

6️⃣ Iniciar o servidor Flask

Ainda dentro da pasta backend, execute:

python app.py

🌐 Endereço do servidor:

http://127.0.0.1:5000

Mantenha o terminal aberto enquanto estiver utilizando o sistema.

7️⃣ Abrir o site

Coloque a pasta Padaria_do_dudu dentro do diretório:

C:\xampp\htdocs\

Depois, acesse:

🔗 http://localhost/Padaria_do_dudu/

O arquivo index.html será a página inicial do sistema.

🔌 Rotas da API

A API utiliza o endereço base:

http://127.0.0.1:5000

Método

Rota

Funcionalidade

🟢 GET

/

Apresenta informações da API.

🟢 GET

/api/clientes

Consulta os clientes.

🔵 POST

/api/clientes

Cadastra clientes.

🟢 GET

/api/funcionarios

Consulta os funcionários.

🔵 POST

/api/funcionarios

Cadastra funcionários.

🟢 GET

/api/produtos

Consulta os produtos.

🔵 POST

/api/produtos

Cadastra produtos.

🟢 GET

/api/pedidos

Consulta os pedidos.

🔵 POST

/api/pedidos

Registra pedidos e seus itens.

🧩 Organização dos arquivos

Arquivo/Pasta

Responsabilidade

index.html

Página inicial do sistema.

backend/app.py

Aplicação Flask e rotas da API.

backend/conexao.py

Conexão com o banco de dados.

backend/testar_conexao.py

Teste de conexão com o MySQL.

backend/daos/dao.py

Operações de acesso ao banco.

backend/models/entidades.py

Classes que representam as entidades.

backend/requirements.txt

Dependências do Python.

database/banco_padaria.sql

Criação do banco e das tabelas.

diagrama_de_classes/

Diagramas conceitual e lógico.

pages/

Páginas de gerenciamento.

script/script.js

Funcionalidades e comunicação com a API.

style/style.css

Estilização das páginas.

⚠️ Observações importantes

O MySQL precisa estar iniciado no XAMPP para acessar o banco.

O servidor Flask precisa estar em execução para utilizar as funcionalidades da API.

O JavaScript utiliza Fetch para se comunicar com http://127.0.0.1:5000.

A configuração de CORS deve permitir a comunicação entre o front-end e o Flask quando executados em origens diferentes.

Os campos enviados pelo JavaScript devem ser compatíveis com os campos esperados pelo back-end.

🎯 Objetivo acadêmico

Desenvolver um sistema funcional integrando conhecimentos de desenvolvimento web, programação orientada a objetos e banco de dados, aplicando na prática os conteúdos estudados em sala de aula.

🏫 Informações do projeto

Informação

Descrição

🏫 Instituição

Colégio UNASP-HT

📚 Projeto

Sistema de Gerenciamento de Padaria

💻 Disciplinas

DWS, POO e Banco de Dados

🎓 Turma

1° TIA

📅 Ano

2026

<p align="center">
  🥖 <strong>Padaria.sys</strong>
  <br>
  Projeto Integrado — 2026
  <br>
  <i>Organização, tecnologia e praticidade para uma padaria.</i>
</p>
