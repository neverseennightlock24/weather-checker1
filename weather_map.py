import os
import sys

import requests
from dotenv import load_dotenv

CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
REQUEST_TIMEOUT_SECONDS = 10


def loadApiKey():
    # The key lives in a git-ignored .env file (or the shell environment)
    load_dotenv()
    apiKey = os.getenv("OPENWEATHERMAP_API_KEY")
    if not apiKey:
        sys.exit("Missing OPENWEATHERMAP_API_KEY. Add it to a .env file in this folder.")
    return apiKey


def fetchWeather(cityName, apiKey):
    # Passing params lets requests URL-encode city names with spaces or accents
    queryParams = {"q": cityName, "appid": apiKey, "units": "metric"}
    response = requests.get(CURRENT_WEATHER_URL, params = queryParams, timeout = REQUEST_TIMEOUT_SECONDS)

    # Distinguish the common failure cases instead of treating every error as a bad city
    if response.status_code == 404:
        raise LookupError(f"City '{cityName}' not found.")
    if response.status_code == 401:
        raise PermissionError("The API key was rejected by OpenWeatherMap.")
    response.raise_for_status()

    return response.json()


def printWeatherReport(weatherData):
    conditions = weatherData["main"]
    windInfo = weatherData["wind"]
    description = weatherData["weather"][0]["description"]

    print(f"City: {weatherData['name']}, {weatherData['sys']['country']}")
    print(f"Temperature: {conditions['temp']}°C")
    print(f"Humidity: {conditions['humidity']}%")
    print(f"Pressure: {conditions['pressure']} hPa")
    print(f"Weather: {description}")
    print(f"Wind Speed: {windInfo['speed']} m/s")


def main():
    apiKey = loadApiKey()

    cityName = input("Enter city name: ").strip()
    if not cityName:
        sys.exit("No city name entered.")

    try:
        weatherData = fetchWeather(cityName, apiKey)
    except (LookupError, PermissionError) as knownError:
        sys.exit(str(knownError))
    except requests.RequestException as networkError:
        sys.exit(f"Could not reach OpenWeatherMap: {networkError}")

    printWeatherReport(weatherData)


if __name__ == "__main__":
    main()
