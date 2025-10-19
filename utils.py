def format_weather(data: dict) -> str:
    """Return a cleanly formatted weather report string."""
    return (
        f"\nWeather in {data['city']}:\n"
        f"🌡️  Temperature: {data['temp']}°C\n"
        f"💧  Humidity: {data['humidity']}%\n"
        f"☁️  Condition: {data['condition']}\n"
    )
