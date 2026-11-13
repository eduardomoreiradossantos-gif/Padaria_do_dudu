🥖 Sistema de Gerenciamento de Pedidos – Padaria

Projeto Integrado – DWS | POO | BD – 2026

📌 Sobre o projeto

O Sistema de Gerenciamento de Pedidos de uma Padaria tem como objetivo organizar e facilitar o controle de clientes, funcionários, produtos e pedidos.

O projeto está sendo desenvolvido como parte do Projeto Integrado das disciplinas de Desenvolvimento Web (DWS), Programação Orientada a Objetos (POO) e Banco de Dados (BD).

🎯 Objetivo

Desenvolver um sistema que permita organizar os dados de uma padaria, utilizando banco de dados MySQL e programação em Python.

🗄️ Banco de Dados

O banco de dados utilizado é o MySQL, com as seguintes tabelas:

clientes: armazena os dados dos clientes.

funcionarios: armazena os dados dos funcionários.

produtos: armazena os produtos disponíveis.

pedidos: registra os pedidos realizados.

itens_pedido: armazena os produtos e quantidades de cada pedido.

🛠️ Tecnologias utilizadas

Python

MySQL

SQL

Git e GitHub

XAMPP

brModelo
=======
# Sistema de Gerenciamento de Pedidos – Padaria

Projeto Integrado de DWS, POO e BD – 2026.

## Etapa 2 — Back-end Python (POO/Flask)

Esta etapa implementa:
- Classes Python para Cliente, Funcionário, Produto, Pedido e ItemPedido.
- DAOs para cadastro e consulta no MySQL.
- API Flask com rotas GET e POST para clientes, funcionários, produtos e pedidos.
- Conexão com o banco MySQL criado na Etapa 1.

## Estrutura

```text
projeto_padaria/
├── diagrama_de_classes/
│   └──conceitual.png
│   └──logico.png
├── database/
│   └── banco_padaria.sql
├── backend/
│   ├── app.py
│   ├── conexao.py
│   ├── requirements.txt
│   ├── testar_conexao.py
│   ├── models/
│   │   └── entidades.py
│   └── daos/
│       └── dao.py
└── README.md
```

## Como executar

1. Inicie o MySQL pelo XAMPP.
2. Importe `database/banco_padaria.sql` no phpMyAdmin.
3. Abra o terminal na pasta `backend`.
4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Teste a conexão:

```bash
python testar_conexao.py
```

6. Inicie a API:

```bash
python app.py
```

A API ficará disponível em `http://127.0.0.1:5000`.

## Rotas disponíveis

| Método | Rota | Função |
|---|---|---|
| GET | `/api/clientes` | Consultar clientes |
| POST | `/api/clientes` | Cadastrar cliente |
| GET | `/api/funcionarios` | Consultar funcionários |
| POST | `/api/funcionarios` | Cadastrar funcionário |
| GET | `/api/produtos` | Consultar produtos |
| POST | `/api/produtos` | Cadastrar produto |
| GET | `/api/pedidos` | Consultar pedidos |
| POST | `/api/pedidos` | Cadastrar pedido com itens |

## Exemplos de cadastro

As rotas POST recebem JSON no corpo da requisição.

Cliente:

```json
{
  "nome": "Maria Silva",
  "telefone": "19999990000",
  "email": "maria@email.com"
}
```

Produto:

```json
{
  "nome": "Pão de queijo",
  "categoria": "salgado",
  "preco": 4.5,
  "disponivel": true
}
```

Pedido (o cliente, funcionário e produto precisam existir no banco):

```json
{
  "id_cliente": 1,
  "id_funcionario": 1,
  "itens": [
    {
      "id_produto": 1,
      "quantidade": 3
    }
  ]
}
```

## Configuração do MySQL

O arquivo `backend/conexao.py` está configurado para o XAMPP padrão:
- Host: `localhost`
- Usuário: `root`
- Senha: vazia
- Banco: `sistema_padaria`

Se seu MySQL usar outra senha, altere o campo `password` em `conexao.py`.

## Observação sobre a Etapa 2

O front-end final não está incluído nesta etapa. A API pode ser testada pelo navegador nas rotas GET e por ferramentas como Thunder Client ou Postman nas rotas POST.
>>>>>>> Stashed changes
