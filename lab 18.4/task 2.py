import requests
import json

def display_weather_details(city):
    api_key = "b99d2574f1dd70cfc8cd1af307c6da15"  # Replace with your actual OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(json.dumps(data, indent=4))
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
city = "London"
display_weather_details(city)
