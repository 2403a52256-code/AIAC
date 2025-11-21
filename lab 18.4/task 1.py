import requests

def display_weather_details(city):
    api_key = 'b99d2574f1dd70cfc8cd1af307c6da15'  # Replace with your actual OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    print(data)

# Example usage:
city = "London"
display_weather_details(city)
