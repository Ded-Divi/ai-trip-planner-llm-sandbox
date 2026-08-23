def get_weather(city: str) -> dict:
    return {
        "city": city,
        "source": "demo local tool",
        "forecast": "No live weather source is connected yet.",
        "verification_needed": True,
    }