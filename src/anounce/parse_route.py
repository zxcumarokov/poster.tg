# Standard Library
import json
from logging import getLogger
from typing import Dict

# Third Party Stuff
import requests

from .abs import AbstractParseRoute


class ParseRouteData(AbstractParseRoute):
    def __init__(
        self,
        base_url: str,
        token: str,
    ):
        self.base_url = base_url
        self.token = token
        self.logger = getLogger(__name__)

    def parse(self, route_database_id: str) -> dict:
        url = f"{self.base_url}/v1/pages/{route_database_id}"

        headers = {
            "Authorization": f"{self.token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
        }
        self.logger.debug(f"Headers: {headers}")

        response = requests.get(url=url, headers=headers, timeout=10)

        if response.status_code != 200:
            raise ValueError(
                f"Request failed with status code {response.status_code}"
                f"and text {response.text}"
            )

        route_properties = json.loads(response.text).get("properties")

        if not route_properties:
            raise ValueError("Route not found")

        return route_properties
