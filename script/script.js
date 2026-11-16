
const API = "http://127.0.0.1:5000/api";

async function buscar(url) {
    const resposta = await fetch(API + url);

    if (!resposta.ok) {
        throw new Error("Erro ao consultar os dados.");
    }

    return await resposta.json();
}

async function enviar(url, dados) {
    const resposta = await fetch(API + url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(dados)
    });

    const resultado = await resposta.json();

    if (!resposta.ok) {
        throw new Error(resultado.erro || "Erro ao cadastrar.");
    }

    return resultado;
}

function mostrarMensagem(id, texto) {
    document.getElementById(id).innerText = texto;
}

async function carregarClientes() {
    const dados = await buscar("/clientes");
    const lista = document.getElementById("listaClientes");

    lista.innerHTML = "";

    dados.forEach(cliente => {
        lista.innerHTML += `
            <tr>
                <td>${cliente.id_cliente}</td>
                <td>${cliente.nome}</td>
                <td>${cliente.telefone || "-"}</td>
                <td>${cliente.email || "-"}</td>
            </tr>
        `;
    });
}

async function carregarProdutos() {
    const dados = await buscar("/produtos");
    const lista = document.getElementById("listaProdutos");

    lista.innerHTML = "";

    dados.forEach(produto => {
        lista.innerHTML += `
            <tr>
                <td>${produto.id_produto}</td>
                <td>${produto.nome}</td>
                <td>${produto.descricao || "-"}</td>
                <td>R$ ${Number(produto.preco).toFixed(2)}</td>
            </tr>
        `;
    });
}

async function carregarFuncionarios() {
    const dados = await buscar("/funcionarios");
    const lista = document.getElementById("listaFuncionarios");

    lista.innerHTML = "";

    dados.forEach(funcionario => {
        lista.innerHTML += `
            <tr>
                <td>${funcionario.id_funcionario}</td>
                <td>${funcionario.nome}</td>
                <td>${funcionario.cargo}</td>
            </tr>
        `;
    });
}

async function carregarPedidos() {
    const dados = await buscar("/pedidos");
    const lista = document.getElementById("listaPedidos");

    lista.innerHTML = "";

    dados.forEach(pedido => {
        lista.innerHTML += `
            <tr>
                <td>${pedido.id_pedido}</td>
                <td>${pedido.cliente}</td>
                <td>${pedido.funcionario}</td>
                <td>${pedido.status}</td>
                <td>R$ ${Number(pedido.total).toFixed(2)}</td>
            </tr>
        `;
    });
}

document.addEventListener("DOMContentLoaded", async function() {

    const pagina = document.body.dataset.page;

    if (pagina === "inicio") {
        try {
            await buscar("/clientes");
            mostrarMensagem("apiStatus", "API conectada com sucesso!");
        } catch (erro) {
            mostrarMensagem("apiStatus", "Não foi possível conectar à API.");
        }
    }

    if (pagina === "clientes") {
        try {
            await carregarClientes();
        } catch (erro) {
            mostrarMensagem("mensagemCliente", erro.message);
        }

        document.getElementById("formCliente").addEventListener("submit", async function(evento) {
            evento.preventDefault();

            const dados = {
                nome: this.nome.value,
                telefone: this.telefone.value,
                email: this.email.value
            };

            try {
                await enviar("/clientes", dados);
                mostrarMensagem("mensagemCliente", "Cliente cadastrado!");
                this.reset();
                await carregarClientes();
            } catch (erro) {
                mostrarMensagem("mensagemCliente", erro.message);
            }
        });
    }

    if (pagina === "produtos") {
        try {
            await carregarProdutos();
        } catch (erro) {
            mostrarMensagem("mensagemProduto", erro.message);
        }

        document.getElementById("formProduto").addEventListener("submit", async function(evento) {
            evento.preventDefault();

            const dados = {
                nome: this.nome.value,
                descricao: this.descricao.value,
                preco: Number(this.preco.value)
            };

            try {
                await enviar("/produtos", dados);
                mostrarMensagem("mensagemProduto", "Produto cadastrado!");
                this.reset();
                await carregarProdutos();
            } catch (erro) {
                mostrarMensagem("mensagemProduto", erro.message);
            }
        });
    }

    if (pagina === "funcionarios") {
        try {
            await carregarFuncionarios();
        } catch (erro) {
            mostrarMensagem("mensagemFuncionario", erro.message);
        }

        document.getElementById("formFuncionario").addEventListener("submit", async function(evento) {
            evento.preventDefault();

            const dados = {
                nome: this.nome.value,
                cargo: this.cargo.value,
                senha: this.senha.value
            };

            try {
                await enviar("/funcionarios", dados);
                mostrarMensagem("mensagemFuncionario", "Funcionário cadastrado!");
                this.reset();
                await carregarFuncionarios();
            } catch (erro) {
                mostrarMensagem("mensagemFuncionario", erro.message);
            }
        });
    }

    if (pagina === "pedidos") {
        try {
            await carregarPedidos();

            const clientes = await buscar("/clientes");
            const funcionarios = await buscar("/funcionarios");
            const produtos = await buscar("/produtos");

            clientes.forEach(c => {
                document.getElementById("pedidoCliente").innerHTML +=
                    `<option value="${c.id_cliente}">${c.nome}</option>`;
            });

            funcionarios.forEach(f => {
                document.getElementById("pedidoFuncionario").innerHTML +=
                    `<option value="${f.id_funcionario}">${f.nome}</option>`;
            });

            produtos.forEach(p => {
                document.getElementById("pedidoProduto").innerHTML +=
                    `<option value="${p.id_produto}">${p.nome}</option>`;
            });

        } catch (erro) {
            mostrarMensagem("mensagemPedido", erro.message);
        }

        document.getElementById("formPedido").addEventListener("submit", async function(evento) {
            evento.preventDefault();

            const dados = {
                id_cliente: Number(this.id_cliente.value),
                id_funcionario: Number(this.id_funcionario.value),
                itens: [{
                    id_produto: Number(this.id_produto.value),
                    quantidade: Number(this.quantidade.value)
                }]
            };

            try {
                await enviar("/pedidos", dados);
                mostrarMensagem("mensagemPedido", "Pedido registrado!");
                this.reset();
                await carregarPedidos();
            } catch (erro) {
                mostrarMensagem("mensagemPedido", erro.message);
            }
        });
    }
});
