from flask import Flask, render_template
import mysql.connector
from config import db_config

app = Flask(__name__)

def get_temperature_data():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, temperature FROM temperature_data ORDER BY timestamp DESC LIMIT 50")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

@app.route('/')
def index():
    data = get_temperature_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)