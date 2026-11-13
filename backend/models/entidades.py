class Cliente:
    def __init__(self, nome, telefone=None, email=None, id_cliente=None):
        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def to_dict(self):
        return {
            "id_cliente": self.id_cliente,
            "nome": self.nome,
            "telefone": self.telefone,
            "email": self.email
        }


class Funcionario:
    def __init__(self, nome, cargo, ativo=True, id_funcionario=None):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.cargo = cargo
        self.ativo = ativo

    def to_dict(self):
        return {
            "id_funcionario": self.id_funcionario,
            "nome": self.nome,
            "cargo": self.cargo,
            "ativo": self.ativo
        }


class Produto:
    def __init__(self, nome, categoria, preco, disponivel=True, id_produto=None):
        self.id_produto = id_produto
        self.nome = nome
        self.categoria = categoria
        self.preco = float(preco)
        self.disponivel = disponivel

    def to_dict(self):
        return {
            "id_produto": self.id_produto,
            "nome": self.nome,
            "categoria": self.categoria,
            "preco": self.preco,
            "disponivel": self.disponivel
        }


class Pedido:
    def __init__(self, id_cliente, id_funcionario, status="em preparo", id_pedido=None):
        self.id_pedido = id_pedido
        self.id_cliente = id_cliente
        self.id_funcionario = id_funcionario
        self.status = status

    def to_dict(self):
        return {
            "id_pedido": self.id_pedido,
            "id_cliente": self.id_cliente,
            "id_funcionario": self.id_funcionario,
            "status": self.status
        }


class ItemPedido:
    def __init__(self, id_produto, quantidade, preco_unitario):
        self.id_produto = id_produto
        self.quantidade = int(quantidade)
        self.preco_unitario = float(preco_unitario)

    def calcular_subtotal(self):
        return self.quantidade * self.preco_unitario

    def to_dict(self):
        return {
            "id_produto": self.id_produto,
            "quantidade": self.quantidade,
            "preco_unitario": self.preco_unitario,
            "subtotal": self.calcular_subtotal()
        }
