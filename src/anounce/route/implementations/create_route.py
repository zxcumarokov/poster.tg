# Standard Library
from logging import getLogger

# My Stuff
from src.anounce.route import Route
from src.anounce.route.abs import AbstractCreateRoute


class CreateRoute(AbstractCreateRoute):
    def __init__(self):
        self.logger = getLogger(__name__)

    def create_route(self, route_properties: dict) -> Route:
        self.logger.debug(f"Route properties: {route_properties}")
        _day_segment = route_properties.get("сегмент дня ", {}).get("url")
        _start_place = route_properties.get("Место старта ", {}).get("url")
        _set_count = route_properties.get("Набор, м", {}).get("number")
        _coffee_break = route_properties.get("кофе брейк ", {}).get("url")
        _distance = route_properties.get("Дистанция", {}).get("number")
        _route_name = (
            route_properties.get("Name", {})
            .get("title", [{}])[0]
            .get("text", {})
            .get("content")
        )

        self.logger.debug(
            f"Day segment: {_day_segment},"
            f"Start place: {_start_place},"
            f"Set count: {_set_count},"
            f"Coffee break: {_coffee_break},"
            f"Distance: {_distance},"
            f"Route name: {_route_name}",
        )

        _route = Route(
            route_name=_route_name,
            distance=_distance,
            climbing=_set_count,
            coffee_break=_coffee_break,
            day_segment=_day_segment,
            start_place=_start_place,
        )
        self.logger.debug(f"Route: {_route}")
        return _route
