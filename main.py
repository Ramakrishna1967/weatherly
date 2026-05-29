from weather import get_weather
from utils import format_weather

def main():
    print(" diabocial weather app")
    city = input("Enter  Fucking city name: ").strip()

    if not city:
        print("City name cannot be empty.")
        return

    data = get_weather(city)
    if data:
        print(format_weather(data))
    else:
        print("Everything is fuckked up")

if __name__ == "__main__":
    main()
