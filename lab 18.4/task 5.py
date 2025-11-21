import requests
import json
import os

def get_and_store_weather(city_name, api_key):
    """
    Fetches weather details of a city using OpenWeatherMap API, displays JSON output,
    and appends the result to 'weather_log.txt' in the current directory.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': 'b99d2574f1dd70cfc8cd1af307c6da15',
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        # Display weather details as JSON
        print(json.dumps(weather_data, indent=4))
        # Append to file
        with open('weather_log.txt', 'a', encoding='utf-8') as f:
            f.write(json.dumps(weather_data) + '\n')
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - {response.text}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error connecting to weather API: {req_err}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:

city = input("Enter city name: ")
get_and_store_weather(city, 'b99d2574f1dd70cfc8cd1af307c6da15')
