# My Stuff
from src.anounce.parse_route import ParseRouteData


def test_parse_route() -> None:
    base_url = "https://api.notion.com"
    token = "Bearer secret_qyo2RS2gK4uMIe77A2U0Ptc7IbvQTSQ7EXr70T1x1sG"

    parse_route = ParseRouteData(base_url, token)

    route_properties = parse_route.parse("ff3ec128-950f-4723-a8a5-6f0e53bfa568")

    assert route_properties
