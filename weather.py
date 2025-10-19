import requests
import os

API_KEY = os.getenv("OPENWEATHER_KEY", "demo")  # store your key as env var

def get_weather(city: str) -> dict | None:
    """Fetch weather data for a given city using OpenWeather API."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"].title(),
        }
    except Exception as e:
        print(f"Error: {e}")
        return None
