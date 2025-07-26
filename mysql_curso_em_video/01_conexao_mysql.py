import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sua_senha",
    database="cadastro"
)

if conexao.is_connected():
    print("Conectado com sucesso ao MySQL!")
conexao.close()
