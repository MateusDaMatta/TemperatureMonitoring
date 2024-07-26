import mysql.connector
from config import db_config

#Conectar ao MySQL
try:
    conn = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password']
    )
    cursor = conn.cursor()
except mysql.connector.Error as err:
    print(f"Erro ao conectar ao MySQL: {err}")

#Criar o banco de dados
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS temp_monitoring")
    print("Banco de dados 'temp_monitoring' criado.")
except mysql.connector.Error as err:
    print(f"Erro ao criar o banco de dados: {err}")

#Selecionar o banco de dados
try:
    conn.database = 'temp_monitoring'
    print("Banco de dados 'temp_monitoring' selecionado.")
except mysql.connector.Error as err:
    print(f"Erro ao selecionar o banco de dados: {err}")

#Criar a tabela
create_table_query = """
CREATE TABLE IF NOT EXISTS temperature_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperature FLOAT NOT NULL
)
"""

try:
    cursor.execute(create_table_query)
    print("Tabela 'temperature_data' criada.")
except mysql.connector.Error as err:
    print(f"Erro ao criar a tabela: {err}")

#Fechar a conexão
cursor.close()
conn.close()
