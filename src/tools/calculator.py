def calculate_daily_budget(total_budget: int, days: int) -> dict:
    if days <= 0:
        raise ValueError("days must be greater than zero")

    return {
        "total_budget": total_budget,
        "days": days,
        "daily_budget": round(total_budget / days, 2),
        "currency": "INR",
    }