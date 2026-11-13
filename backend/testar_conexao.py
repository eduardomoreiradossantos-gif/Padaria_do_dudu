from conexao import conectar

con = conectar()

if con:
    print("Conexão com o banco realizada com sucesso!")
    cursor = con.cursor()
    cursor.execute("SELECT COUNT(*) FROM produtos")
    print("Produtos cadastrados:", cursor.fetchone()[0])
    cursor.close()
    con.close()
else:
    print("Falha na conexão. Confira o XAMPP e o banco sistema_padaria.")
