# Third Party Stuff
from pydantic import BaseModel


class Route(BaseModel):
    route_name: str | None = None
    distance: float | None = None  # km
    climbing: float | None = None  # m
    coffee_break: str | None = None  # url 2gis
    day_segment: str | None = None  # url strava
    start_place: str | None = None  # url 2gis
