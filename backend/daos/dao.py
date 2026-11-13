from conexao import conectar


class ClienteDAO:
    def listar(self):
        con = conectar()
        if not con:
            raise RuntimeError("Não foi possível conectar ao banco.")
        try:
            cur = con.cursor(dictionary=True)
            cur.execute("SELECT id_cliente, nome, telefone, email FROM clientes ORDER BY id_cliente")
            return cur.fetchall()
        finally:
            cur.close()
            con.close()

    def inserir(self, cliente):
        con = conectar()
        if not con:
            raise RuntimeError("Não foi possível conectar ao banco.")
        try:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO clientes (nome, telefone, email) VALUES (%s, %s, %s)",
                (cliente.nome, cliente.telefone, cliente.email)
            )
            con.commit()
            return cur.lastrowid
        finally:
            cur.close()
            con.close()


class FuncionarioDAO:
    def listar(self):
        con = conectar()
        if not con:
            raise RuntimeError("Não foi possível conectar ao banco.")
        try:
            cur = con.cursor(dictionary=True)
            cur.execute("SELECT id_funcionario, nome, cargo, ativo FROM funcionarios ORDER BY id_funcionario")
            return cur.fetchall()
        finally:
            cur.close()
            con.close()

    def inserir(self, funcionario):
        con = conectar()
        if not con:
            raise RuntimeError("Não foi possível conectar ao banco.")
        try:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO funcionarios (nome, cargo, ativo) VALUES (%s, %s, %s)",
                (funcionario.nome, funcionario.cargo, funcionario.ativo)
            )
            con.commit()
            return cur.lastrowid
        finally:
            cur.close()
            con.close()


class ProdutoDAO:
    def listar(self):
        con = conectar()
        if not con:
            raise RuntimeError("Não foi possível conectar ao banco.")
        try:
            cur = con.cursor(dictionary=True)
            cur.execute(
                "SELECT id_produto, nome, categoria, preco, disponivel "
                "FROM produtos ORDER BY id_produto"
            )
            return cur.fetchall()
        finally:
            cur.close()
            con.close()

    def inserir(self, produto):
        con = conectar()
        if not con:
            raise RuntimeError("Não foi possível conectar ao banco.")
        try:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO produtos (nome, categoria, preco, disponivel) VALUES (%s, %s, %s, %s)",
                (produto.nome, produto.categoria, produto.preco, produto.disponivel)
            )
            con.commit()
            return cur.lastrowid
        finally:
            cur.close()
            con.close()


class PedidoDAO:
    def listar(self):
        con = conectar()
        if not con:
            raise RuntimeError("Não foi possível conectar ao banco.")
        try:
            cur = con.cursor(dictionary=True)
            cur.execute("""
                SELECT p.id_pedido, p.data_pedido, p.status,
                       p.id_cliente, c.nome AS cliente,
                       p.id_funcionario, f.nome AS funcionario,
                       COALESCE(SUM(ip.quantidade * ip.preco_unitario), 0) AS total
                FROM pedidos p
                INNER JOIN clientes c ON c.id_cliente = p.id_cliente
                INNER JOIN funcionarios f ON f.id_funcionario = p.id_funcionario
                LEFT JOIN itens_pedido ip ON ip.id_pedido = p.id_pedido
                GROUP BY p.id_pedido, p.data_pedido, p.status,
                         p.id_cliente, c.nome, p.id_funcionario, f.nome
                ORDER BY p.id_pedido DESC
            """)
            return cur.fetchall()
        finally:
            cur.close()
            con.close()

    def inserir(self, id_cliente, id_funcionario, itens):
        con = conectar()
        if not con:
            raise RuntimeError("Não foi possível conectar ao banco.")
        cur = con.cursor(dictionary=True)
        try:
            # Confere os registros relacionados antes de criar o pedido.
            cur.execute("SELECT id_cliente FROM clientes WHERE id_cliente = %s", (id_cliente,))
            if not cur.fetchone():
                raise ValueError("Cliente não encontrado.")

            cur.execute(
                "SELECT id_funcionario FROM funcionarios WHERE id_funcionario = %s AND ativo = TRUE",
                (id_funcionario,)
            )
            if not cur.fetchone():
                raise ValueError("Funcionário não encontrado ou inativo.")

            if not isinstance(itens, list) or len(itens) == 0:
                raise ValueError("O pedido precisa ter pelo menos um item.")

            cur.execute(
                "INSERT INTO pedidos (id_cliente, id_funcionario) VALUES (%s, %s)",
                (id_cliente, id_funcionario)
            )
            id_pedido = cur.lastrowid

            for item in itens:
                id_produto = int(item["id_produto"])
                quantidade = int(item["quantidade"])
                if quantidade <= 0:
                    raise ValueError("A quantidade deve ser maior que zero.")

                cur.execute(
                    "SELECT preco, disponivel FROM produtos WHERE id_produto = %s",
                    (id_produto,)
                )
                produto = cur.fetchone()
                if not produto or not produto["disponivel"]:
                    raise ValueError(f"Produto {id_produto} não encontrado ou indisponível.")

                cur.execute("""
                    INSERT INTO itens_pedido
                    (id_pedido, id_produto, quantidade, preco_unitario)
                    VALUES (%s, %s, %s, %s)
                """, (id_pedido, id_produto, quantidade, produto["preco"]))

            con.commit()
            return id_pedido
        except Exception:
            con.rollback()
            raise
        finally:
            cur.close()
            con.close()
