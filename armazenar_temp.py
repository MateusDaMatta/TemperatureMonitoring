#Para arduino

from flask import Flask, request
import mysql.connector
from config import db_config

app = Flask(__name__)

@app.route('/store_temperature', methods=['GET'])
def store_temperature():
    temperature = request.args.get('temperature')
    if temperature:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO temperature_data (temperature) VALUES (%s)", (temperature,))
        conn.commit()
        cursor.close()
        conn.close()
        return 'Temperatura armazenada com sucesso.', 200
    else:
        return 'Dados de temperatura ausentes.', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
