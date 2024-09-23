from flask import Flask, jsonify, request
import requests
import urllib.parse
import os
import logging

# Construindo a chave API para a API do OpenWeatherMap
API_KEY = os.environ.get("OPENWEATHERMAP_API_KEY")

# Criando um aplicativo Flask
app = Flask(__name__)

# Configurando o logging com nível de depuração
logging.basicConfig(level=logging.DEBUG)


def kelvin_to_celsius(kelvin: float) -> float:
    """
    Converte temperatura de Kelvin para Celsius
    :param kelvin: Temperatura em Kelvin
    :return: Temperatura em Celsius
    """
    # Verificando se a entrada é um número
    if not isinstance(kelvin, (int, float)):
        raise ValueError("Temperatura deve ser um número")
    # Convertendo Kelvin para Celsius
    return kelvin - 273.15


def get_weather_data(city: str, country: str) -> dict:
    """
    Obtém dados de clima para uma cidade e país
    :param city: Nome da cidade
    :param country: Nome do país
    :return: Dados de clima em formato JSON
    """
    # Codificando o nome da cidade para URL
    city_encoded = urllib.parse.quote(city)
    # Construindo a URL da API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={
        city_encoded},{country}&lang=pt&appid={API_KEY}"
    try:
        # Enviando solicitação GET para a API
        response = requests.get(url, timeout=10)
        # Verificando se a resposta é OK
        response.raise_for_status()
        # Analisando a resposta JSON
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as ReqEx:
        # Registrando erro se a solicitação da API falhar
        logging.error("Erro ao obter dados de clima: %s", ReqEx)
        # Retornando resposta de erro com código de status 500
        return jsonify({"error": f"Erro ao obter dados de clima: {ReqEx}"}), 500


def convert_weather_data(weather_data: dict) -> dict:
    """
    Converte dados de clima de Kelvin para Celsius
    :param weather_data: Dados de clima em formato JSON
    :return: Dados de clima com temperaturas em Celsius
    """
    # Obtendo os dados de clima principais
    main_data = weather_data.get("main")
    if main_data:
        # Convertendo temperaturas de Kelvin para Celsius
        main_data["temp"] = kelvin_to_celsius(main_data["temp"])
        main_data["temp_max"] = kelvin_to_celsius(main_data["temp_max"])
        main_data["temp_min"] = kelvin_to_celsius(main_data["temp_min"])
    return weather_data


def validate_input(city: str, country: str) -> bool:
    """
    Valida se a cidade e o país têm um formato válido
    :param city: Nome da cidade
    :param country: Nome do país
    :return: True se a entrada for válida, False caso contrário
    """
    # Verificando se a cidade e o país não estão vazios
    if not city or not country:
        return False
    # Verificando se a cidade e o país são strings
    if not isinstance(city, str) or not isinstance(country, str):
        return False
    # Verificando se a cidade e o país têm pelo menos 2 caracteres
    if len(city) < 2 or len(country) < 2:
        return False
    # Adicionando mais regras de validação aqui, se necessário
    return True


@app.route("/weather", methods=["GET"])
def weather():
    """
    Manipula solicitação GET para o endpoint /weather
    """
    # Obtendo a cidade e o país dos parâmetros de consulta
    city = request.args.get("city")
    country = request.args.get("country")
    # Validando a entrada
    if not validate_input(city, country):
        # Retornando resposta de erro com código de status 400
        return jsonify({"error": "Cidade e país devem ser strings válidas"}), 400
    # Obtendo os dados de clima
    weather_data = get_weather_data(city, country)
    # Verificando se os dados de clima têm um erro
    if "error" in weather_data:
        # Retornando resposta de erro com código de status 500
        return jsonify(weather_data), 500
    # Convertendo os dados de clima para Celsius
    weather_data = convert_weather_data(weather_data)
    # Retornando os dados de clima em formato JSON
    return jsonify(weather_data)


if __name__ == "__main__":
    # Executando o aplicativo Flask
    app.run()
