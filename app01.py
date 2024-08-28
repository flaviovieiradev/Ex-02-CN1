import mysql.connector

db = mysql.connector.connect(
    host='104.41.46.45',
    user="flavio",
    password="123456",
    database="BD01"
)

# Crie um cursor para executar as consultas
cursor = db.cursor()

# Dados do usuário a ser inserido
# nome = input("Digite seu nome: ")
nome = "Louro José"
usuario = "ljose"
senha = "lourojose123"
email = "lourojose@lourojose.com"

# Construa a consulta SQL
sql = "INSERT INTO usuario (nome, usuario, senha, email) VALUES (%s, %s, %s, %s)"
valores = (nome, usuario, senha, email)

# Execute a consulta
cursor.execute(sql, valores)

# Confirme as alterações
db.commit()

# Feche a conexão
db.close()

# print("Olá,", name)
