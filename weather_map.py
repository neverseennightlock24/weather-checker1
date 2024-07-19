import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Replace with your actual OpenWeatherMap API key
API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]
        
        print(f"City: {data['name']}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Weather: {weather['description']}")
        print(f"Wind Speed: {wind['speed']} m/s")
        
    else:
        print("City not found.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
