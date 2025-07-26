import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sua_senha",
    database="cadastro"
)

cursor = conexao.cursor()
cursor.execute("SELECT * FROM pessoas")

for (id, nome, idade) in cursor.fetchall():
    print(f"{id}: {nome} - {idade} anos")

cursor.close()
conexao.close()
