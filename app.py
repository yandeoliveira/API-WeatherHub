from flask import Flask, jsonify, request
import requests

API_KEY = "0f5deb3f9383315c697b441de7af27af"

app = Flask(__name__)


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city")
    country = request.args.get("country")
    weather_data = get_weather(city, country)
    return jsonify(weather_data)


def get_weather(city, country):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={
        city},{country}&appid={API_KEY}"
    response = requests.get(url, timeout=10)
    data = response.json()

    # Converter temperaturas de Kelvin para Celsius
    main_data = data.get("main")
    if main_data:
        main_data["temp"] = kelvin_to_celsius(main_data["temp"])
        main_data["temp_max"] = kelvin_to_celsius(main_data["temp_max"])
        main_data["temp_min"] = kelvin_to_celsius(main_data["temp_min"])

    return data


if __name__ == "__main__":
    app.run()
