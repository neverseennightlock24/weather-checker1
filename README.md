# weather-checker1
Checks the current weather of any city in the world using the [OpenWeatherMap](https://openweathermap.org/) API.

## Setup
1. Install the dependencies:
   ```
   python3 -m pip install -r requirements.txt
   ```
2. Get a free API key from [OpenWeatherMap](https://home.openweathermap.org/api_keys).
3. Create a file named `.env` in this folder containing:
   ```
   OPENWEATHERMAP_API_KEY=your_key_here
   ```
   `.env` is git-ignored, so your key stays out of the repository.

## Usage
```
python3 weather_map.py
```
Enter a city name when prompted to see its temperature, humidity, pressure, conditions, and wind speed.
