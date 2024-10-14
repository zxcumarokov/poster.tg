# Third Party Stuff
from pydantic import BaseModel


class Route(BaseModel):
    route_name: str
    distance: float
    set_count: float
    coffee_break: str
    day_segment: str
    start_place: str
