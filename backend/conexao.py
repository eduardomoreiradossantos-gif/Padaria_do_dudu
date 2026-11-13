import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistema_padaria"
        )
    except Error as erro:
        print("Erro ao conectar ao banco:", erro)
        return None
