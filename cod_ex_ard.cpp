#include <ESP8266WiFi.h>
#include <DHT.h>

#define DHTPIN D2      // Pino ao qual o sensor está conectado
#define DHTTYPE DHT22  // Tipo do sensor

DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "SEU_SSID";       // Substitua pelo seu SSID do wifi
const char* password = "SUA_SENHA"; // Substitua pela sua senha do wifi
const char* serverName = "http://seuserver.com/submit_data"; // URL do servidor

void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Conectado ao Wifi");
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Falha ao ler o sensor DHT!");
    return;
  }

  WiFiClient client;
  if (client.connect(serverName, 80)) {
    String postData = "temperature=" + String(temperature) + "&humidity=" + String(humidity);
    client.println("POST /submit_data HTTP/1.1");
    client.println("Host: yourserver.com");
    client.println("Content-Type: application/x-www-form-urlencoded");
    client.println("Content-Length: " + String(postData.length()));
    client.println();
    client.println(postData);
  }
  delay(60000); // envia dados a cada 60 segundos
}
