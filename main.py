from weather import get_weather
from utils import format_weather

def main():
    print("🌤️  Simple Weather App")
    city = input("Enter city name: ").strip()

    if not city:
        print("City name cannot be empty.")
        return

    data = get_weather(city)
    if data:
        print(format_weather(data))
    else:
        print("Could not fetch weather data. Check your city name or connection.")

if __name__ == "__main__":
    main()
