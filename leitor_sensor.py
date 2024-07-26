import mysql.connector
import Adafruit_DHT
import time
from config import db_config

sensor = Adafruit_DHT.DHT22
pin = 4  #Pino GPIO conectado ao sensor

def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return temperature

def store_temperature(temp):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO temperature_data (temperature) VALUES (%s)", (temp,))
    conn.commit()
    cursor.close()
    conn.close()

while True:
    temperature = read_sensor()
    if temperature is not None:
        store_temperature(temperature)
        print(f'Temperatura armazenada: {temperature:.2f}°C')
    else:
        print('Falha na leitura do sensor')
    time.sleep(60)  #Leitura a cada 60 segundos