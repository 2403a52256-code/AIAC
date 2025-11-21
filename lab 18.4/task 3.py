import requests
import json

def display_weather_details(city):
    api_key = "b99d2574f1dd70cfc8cd1af307c6da15"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        # Display full JSON output
        print("Full API response:")
        print(json.dumps(data, indent=4))
        
        # Extract and display key weather details
        if data.get("cod") != 200:
            print(f"Error fetching weather for '{city}': {data.get('message', 'No additional info')}")
            return
        
        weather_desc = data.get("weather", [{}])[0].get("description", "No description")
        temp = data.get("main", {}).get("temp", "N/A")
        humidity = data.get("main", {}).get("humidity", "N/A")
        
        print("\nWeather Summary:")
        print(f"City        : {data.get('name', 'Unknown')}")
        print(f"Description : {weather_desc.capitalize()}")
        print(f"Temperature : {temp}°C")
        print(f"Humidity    : {humidity}%")
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    city = input("Enter city name: ")
    display_weather_details(city)
