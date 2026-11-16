# 🥖 Sistema de Gerenciamento de Pedidos – Padaria

**Projeto Integrado – DWS | POO | BD – 2026**

---

## 📌 Sobre o projeto

O Sistema de Gerenciamento de Pedidos de uma Padaria tem como objetivo organizar e facilitar o controle de clientes, funcionários, produtos e pedidos.

O projeto está sendo desenvolvido como parte do Projeto Integrado das disciplinas de Desenvolvimento Web (DWS), Programação Orientada a Objetos (POO) e Banco de Dados (BD).

## 🎯 Objetivo

Desenvolver um sistema para gerenciamento de uma padaria, integrando banco de dados MySQL, programação orientada a objetos com Python e uma interface web desenvolvida com HTML, CSS e JavaScript.

## 🗄️ Banco de Dados

O banco de dados utilizado é o **MySQL**, com o nome `sistema_padaria`.

O projeto possui as seguintes tabelas:

- 👥 **clientes:** armazena os dados dos clientes.
- 👨‍🍳 **funcionarios:** armazena os dados dos funcionários.
- 🥐 **produtos:** armazena os produtos disponíveis na padaria.
- 🛒 **pedidos:** registra os pedidos realizados.
- 📦 **itens_pedido:** armazena os produtos e as quantidades de cada pedido.

## 🛠️ Tecnologias utilizadas

- 🐍 Python
- 🔥 Flask
- 🗄️ MySQL
- 💾 SQL
- 🌐 HTML5
- 🎨 CSS3
- ⚡ JavaScript
- 🖥️ XAMPP
- 🐙 Git e GitHub
- 📊 brModelo

## 📁 Estrutura do projeto

```text
Padaria_do_dudu/
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
```

## ⚙️ Como executar o banco de dados

1. Instale e abra o **XAMPP**.
2. Inicie os serviços **Apache** e **MySQL**.
3. Acesse o phpMyAdmin pelo endereço `http://localhost/phpmyadmin`.
4. Clique na aba **Importar**.
5. Selecione o arquivo `database/banco_padaria.sql`.
6. Clique em **Executar**.
7. O banco `sistema_padaria` será criado com suas respectivas tabelas.

## 🐍 Conexão com Python

O arquivo responsável pela conexão com o banco de dados é:

`backend/conexao.py`

Para instalar as dependências do projeto, abra o terminal na pasta principal e execute:

```bash
cd backend
pip install -r requirements.txt
```

Para testar a conexão com o MySQL, execute:

```bash
python testar_conexao.py
```

Para iniciar o servidor Flask, execute:

```bash
python app.py
```

O servidor será iniciado no endereço:

`http://127.0.0.1:5000`

## 🌐 Execução do site

Para acessar o sistema pelo XAMPP:

1. Coloque a pasta `Padaria_do_dudu` dentro de `C:\xampp\htdocs`.
2. Inicie o Apache pelo XAMPP.
3. Inicie o MySQL pelo XAMPP.
4. Execute o servidor Flask pelo terminal.
5. Acesse o endereço:

`http://localhost/Padaria_do_dudu/`

O arquivo `index.html` é a página inicial do sistema.

## 🔌 Rotas da API

| Método | Rota | Funcionalidade |
|:---:|---|---|
| GET | `/api/clientes` | Consultar clientes |
| POST | `/api/clientes` | Cadastrar clientes |
| GET | `/api/produtos` | Consultar produtos |
| POST | `/api/produtos` | Cadastrar produtos |
| GET | `/api/funcionarios` | Consultar funcionários |
| POST | `/api/funcionarios` | Cadastrar funcionários |
| GET | `/api/pedidos` | Consultar pedidos |
| POST | `/api/pedidos` | Registrar pedidos |

## 📚 Etapas do projeto

| Etapa | Entrega |
|:---:|---|
| 📝 **Etapa 1** | Modelagem do banco de dados e diagramas conceitual e lógico. |
| 💻 **Etapa 2** | Desenvolvimento do back-end em Python, POO, DAOs e Flask. |
| 🚀 **Entrega Final** | Integração do banco de dados, back-end e front-end com HTML, CSS e JavaScript. |

## 👨‍💻 Projeto Integrado

Trabalho desenvolvido para as disciplinas de **Desenvolvimento Web (DWS), Programação Orientada a Objetos (POO) e Banco de Dados (BD)**.

**Instituição:** Colégio UNASP-HT  
**Turma:** 2° TIA  
**Ano:** 2026

---

<p align="center">
  🥖 <strong>Sistema de Gerenciamento de Pedidos – Padaria</strong>
  <br>
  <i>Projeto Integrado – 2026</i>
</p>
