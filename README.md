# Monitoramento de Temperatura com Arduino e Flask

Este projeto demonstra como monitorar e armazenar dados de temperatura usando um sensor de temperatura conectado a um Arduino ou ESP8266 e um servidor Python Flask. Os dados são armazenados em um banco de dados MySQL e podem ser visualizados através de uma interface web.

## Componentes

- **Arduino ou ESP8266**: Placa de desenvolvimento para ler os dados do sensor de temperatura.
- **Sensor de Temperatura DHT22**: Sensor que mede a temperatura e umidade.
- **Servidor Python Flask**: Recebe e armazena os dados do sensor.
- **Banco de Dados MySQL**: Armazena os dados de temperatura.

## Estrutura do Projeto

1. **`config.py`**: Contém as configurações de conexão com o banco de dados MySQL.
2. **`create_db.py`**: Script para criar o banco de dados e a tabela necessária.
3. **`leitor_sensor.py`**: Script para ler dados do sensor e armazená-los no banco de dados.
4. **`app.py`**: Servidor Flask que exibe os dados armazenados em uma interface web.
5. **`index.html`**: Página HTML para visualizar os dados de temperatura.
6. **`style.css`**: Arquivo de estilo para a página HTML.

## Configuração

1. **Instalar Dependências**

   Certifique-se de ter o Python instalado e instale as dependências necessárias:

   ```bash
   pip install flask mysql-connector-python
