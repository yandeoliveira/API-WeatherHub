from flask import Flask, jsonify, request
import requests
import urllib.parse
import os

API_KEY = os.environ.get("OPENWEATHERMAP_API_KEY")

app = Flask(__name__)  # Adicione essa linha


def kelvin_to_celsius(kelvin: float) -> float:
    """Converte temperatura de Kelvin para Celsius"""
    return kelvin - 273.15


def get_weather_data(city: str, country: str) -> dict:
    """Obtém dados de clima para uma cidade e país"""
    city_encoded = urllib.parse.quote(city)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={
        city_encoded},{country}&lang=pt&appid={API_KEY}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        return {"error": f"Erro ao obter dados de clima: {e}"}


def convert_weather_data(weather_data: dict) -> dict:
    """Converte dados de clima para Celsius"""
    main_data = weather_data.get("main")
    if main_data:
        main_data["temp"] = kelvin_to_celsius(main_data["temp"])
        main_data["temp_max"] = kelvin_to_celsius(main_data["temp_max"])
        main_data["temp_min"] = kelvin_to_celsius(main_data["temp_min"])
    return weather_data


@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city")
    country = request.args.get("country")
    if not city or not country:
        return jsonify({"error": "City and country are required"}), 400
    if not isinstance(city, str) or not isinstance(country, str):
        return jsonify({"error": "City and country must be strings"}), 400
    weather_data = get_weather_data(city, country)
    weather_data = convert_weather_data(weather_data)
    return jsonify(weather_data)


if __name__ == "__main__":
    app.run()
