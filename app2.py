from flask import Flask, jsonify, request
import requests
import urllib.parse

API_KEY = "0f5deb3f9383315c697b441de7af27af"

app = Flask(__name__)


def kelvin_to_celsius(kelvin: float) -> float:
    return kelvin - 273.15


def get_weather_data(city: str, country: str) -> dict:
    city_encoded = urllib.parse.quote(city)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_encoded},{country}&lang=pt&appid={API_KEY}"
    print(url)
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Tratamento de erros
    weather_data = response.json()
    return weather_data


def convert_weather_data(weather_data: dict) -> dict:
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
    weather_data = get_weather_data(city, country)
    weather_data = convert_weather_data(weather_data)
    return jsonify(weather_data)


if __name__ == "__main__":
    app.run()
