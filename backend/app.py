from flask import Flask, jsonify, request
from mysql.connector import Error

from models.entidades import Cliente, Funcionario, Produto
from daos.dao import ClienteDAO, FuncionarioDAO, ProdutoDAO, PedidoDAO

app = Flask(__name__)

cliente_dao = ClienteDAO()
funcionario_dao = FuncionarioDAO()
produto_dao = ProdutoDAO()
pedido_dao = PedidoDAO()


def erro_servidor(erro):
    print("Erro:", erro)
    return jsonify({"erro": "Não foi possível concluir a operação. Confira o banco de dados."}), 500


@app.get("/")
def inicio():
    return jsonify({
        "mensagem": "API do Sistema da Padaria funcionando!",
        "rotas": [
            "GET /api/clientes", "POST /api/clientes",
            "GET /api/funcionarios", "POST /api/funcionarios",
            "GET /api/produtos", "POST /api/produtos",
            "GET /api/pedidos", "POST /api/pedidos"
        ]
    })


@app.get("/api/clientes")
def listar_clientes():
    try:
        return jsonify(cliente_dao.listar())
    except (Error, RuntimeError) as erro:
        return erro_servidor(erro)


@app.post("/api/clientes")
def cadastrar_cliente():
    dados = request.get_json(silent=True) or {}
    if not dados.get("nome"):
        return jsonify({"erro": "O nome do cliente é obrigatório."}), 400
    try:
        cliente = Cliente(dados["nome"], dados.get("telefone"), dados.get("email"))
        novo_id = cliente_dao.inserir(cliente)
        return jsonify({"mensagem": "Cliente cadastrado com sucesso.", "id_cliente": novo_id}), 201
    except (Error, RuntimeError) as erro:
        return erro_servidor(erro)


@app.get("/api/funcionarios")
def listar_funcionarios():
    try:
        return jsonify(funcionario_dao.listar())
    except (Error, RuntimeError) as erro:
        return erro_servidor(erro)


@app.post("/api/funcionarios")
def cadastrar_funcionario():
    dados = request.get_json(silent=True) or {}
    if not dados.get("nome") or not dados.get("cargo"):
        return jsonify({"erro": "Nome e cargo são obrigatórios."}), 400
    try:
        funcionario = Funcionario(
            dados["nome"], dados["cargo"], dados.get("ativo", True)
        )
        novo_id = funcionario_dao.inserir(funcionario)
        return jsonify({"mensagem": "Funcionário cadastrado com sucesso.", "id_funcionario": novo_id}), 201
    except (Error, RuntimeError) as erro:
        return erro_servidor(erro)


@app.get("/api/produtos")
def listar_produtos():
    try:
        return jsonify(produto_dao.listar())
    except (Error, RuntimeError) as erro:
        return erro_servidor(erro)


@app.post("/api/produtos")
def cadastrar_produto():
    dados = request.get_json(silent=True) or {}
    obrigatorios = ["nome", "categoria", "preco"]
    if any(campo not in dados for campo in obrigatorios):
        return jsonify({"erro": "Nome, categoria e preço são obrigatórios."}), 400
    try:
        preco = float(dados["preco"])
        if preco < 0:
            return jsonify({"erro": "O preço não pode ser negativo."}), 400
        produto = Produto(
            dados["nome"], dados["categoria"], preco,
            dados.get("disponivel", True)
        )
        novo_id = produto_dao.inserir(produto)
        return jsonify({"mensagem": "Produto cadastrado com sucesso.", "id_produto": novo_id}), 201
    except (ValueError, TypeError):
        return jsonify({"erro": "O preço informado é inválido."}), 400
    except (Error, RuntimeError) as erro:
        return erro_servidor(erro)


@app.get("/api/pedidos")
def listar_pedidos():
    try:
        return jsonify(pedido_dao.listar())
    except (Error, RuntimeError) as erro:
        return erro_servidor(erro)


@app.post("/api/pedidos")
def cadastrar_pedido():
    dados = request.get_json(silent=True) or {}
    if not dados.get("id_cliente") or not dados.get("id_funcionario") or not dados.get("itens"):
        return jsonify({
            "erro": "Informe id_cliente, id_funcionario e uma lista de itens."
        }), 400
    try:
        novo_id = pedido_dao.inserir(
            int(dados["id_cliente"]),
            int(dados["id_funcionario"]),
            dados["itens"]
        )
        return jsonify({"mensagem": "Pedido cadastrado com sucesso.", "id_pedido": novo_id}), 201
    except (ValueError, KeyError, TypeError) as erro:
        return jsonify({"erro": str(erro)}), 400
    except (Error, RuntimeError) as erro:
        return erro_servidor(erro)


if __name__ == "__main__":
    app.run(debug=True)
