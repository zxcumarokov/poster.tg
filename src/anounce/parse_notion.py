# Standard Library
from datetime import datetime

# Third Party Stuff
import requests

# My Stuff
from src.anounce.abcparse_notion import AbstractParseNotion
from src.models.notion_calendar.calendar import Ride


class ParseNotion(AbstractParseNotion):
    def __init__(self, url: str) -> None:
        self.url = url

    def parse(self, date: datetime) -> Ride:
        json_parse = '{"channel": "Ride", "route_url": "Ride"}'
        ride = Ride.model_validate_json(json_parse)

        return ride
