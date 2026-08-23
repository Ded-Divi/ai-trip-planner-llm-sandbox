from pydantic import BaseModel


class DailyItinerary(BaseModel):
    day: int
    headline: str
    activities: list[str]


class TripPlan(BaseModel):
    destination: str
    days: int
    summary: str
    daily_itinerary: list[DailyItinerary]
    recommendations: list[str]
    assumptions: list[str]
    verification_needed: list[str]