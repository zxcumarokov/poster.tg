# Standard Library
import json
from logging import getLogger

# Third Party Stuff
import requests

from ..abs import AbstractParseRoute


class ParseRouteData(AbstractParseRoute):
    def __init__(
        self,
        notion_base_url: str,
        notion_token: str,
    ):
        self.base_url = notion_base_url
        self.token = notion_token
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

        self.logger.debug(f"Response: {response.text}")

        if response.status_code != 200:
            raise ValueError(
                f"Request failed with status code {response.status_code}"
                f"and text {response.text}"
            )

        route_properties = json.loads(response.text).get("properties")

        if not route_properties:
            raise ValueError("Route not found")

        return route_properties
