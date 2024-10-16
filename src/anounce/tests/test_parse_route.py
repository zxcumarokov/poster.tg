# Standard Library
from os import getenv

# My Stuff
from src.anounce.route.implementations import ParseRouteData

DB_ID = "ff3ec128-950f-4723-a8a5-6f0e53bfa568"


def test_parse_route() -> None:
    base_url = "https://api.notion.com"
    token = getenv("NOTION_TOKEN")

    if not token:
        raise ValueError("NOTION_TOKEN не установлен или пуст.")

    parse_route = ParseRouteData(base_url, token)

    route_properties = parse_route.parse(DB_ID)

    assert route_properties
