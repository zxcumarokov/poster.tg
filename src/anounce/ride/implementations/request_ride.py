# Standard Library
import json
from datetime import datetime
from logging import getLogger
from typing import Dict

# Third Party Stuff
import requests

# My Stuff
from src.anounce.ride.abs import AbstractRequestRide


class RequestRide(AbstractRequestRide):
    def __init__(
        self,
        url: str,
        token: str,
        notion_version: str,
    ) -> None:
        self.url = url
        self.token = token
        self.notion_version = notion_version
        self.logger = getLogger(__name__)

    def parse(self, date: datetime) -> Dict:
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": self.notion_version,
            "Content-Type": "application/json",
        }
        date_str = date.strftime("%Y-%m-%d")
        data = {"filter": {"property": "Date", "date": {"equals": date_str}}}
        self.logger.info(f"Request: {data}")
        response = requests.post(
            url=self.url,
            headers=headers,
            json=data,
            timeout=10,
        )

        self.logger.info(f"Response: {response.text}")
        rides_list = json.loads(response.text)["results"]
        if not rides_list:
            raise ValueError("No rides found")

        self.logger.info(f"Response ride list: {rides_list}")

        response_ride_properties = rides_list[0]["properties"]
        self.logger.info(f"Response: {response_ride_properties}")
        return response_ride_properties
