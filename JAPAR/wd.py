import requests

def get_weather(api_key, latitude, longitude):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': latitude,
        'lon': longitude,
        'appid': api_key,
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        location = weather_data['name']
        main_weather = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        print(f"Location: {location}")
        print(f"Weather: {main_weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"Failed to get weather data. Status code: {response.status_code}")

# Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
api_key = '1f43de1fa821c08b230c106118aafe82'
latitude = 30.504963
longitude = 47.838486

get_weather(api_key, latitude, longitude)
