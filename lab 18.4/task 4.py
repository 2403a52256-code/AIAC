import requests

def display_weather_details(city):
    api_key = "b99d2574f1dd70cfc8cd1af307c6da15"  # Replace with your actual OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get("cod") != 200:
            print(f"Error fetching weather for '{city}': {data.get('message', 'No additional info')}")
            return

        weather = data.get("weather", [{}])[0].get("description", "No description")
        temp = data.get("main", {}).get("temp", "N/A")
        feels_like = data.get("main", {}).get("feels_like", "N/A")
        humidity = data.get("main", {}).get("humidity", "N/A")
        wind_speed = data.get("wind", {}).get("speed", "N/A")
        print(f"Weather in {city}:")
        print(f"  Description : {weather.capitalize()}")
        print(f"  Temperature : {temp}°C (feels like {feels_like}°C)")
        print(f"  Humidity    : {humidity}%")
        print(f"  Wind Speed  : {wind_speed} m/s")
        print("-" * 40)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred for '{city}': {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred for '{city}': {err}")
    except Exception as e:
        print(f"An unexpected error occurred for '{city}': {e}")

# Test cases
test_cities = ["London", "New York", "InvalidCity123"]
for city in test_cities:
    display_weather_details(city)

