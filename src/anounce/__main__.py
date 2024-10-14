# Standard Library
import os
from datetime import (
    datetime,
    timezone,
)

# Third Party Stuff
from dotenv import load_dotenv
from telebot import TeleBot

# My Stuff
from src.anounce.anounce_view import AnounceView
from src.anounce.get_route_id import GetRouteId
from src.anounce.parse_route import ParseRouteData

from .create_ride import CreateRide
from .create_route import CreateRoute
from .parse_notion import ParseNotion
from .send_anounce import SendAnounce

load_dotenv()
anounce_bot = TeleBot(os.getenv("BOT_TOKEN", ""))
if not anounce_bot:
    raise ValueError("BOT_TOKEN не установлен или пуст.")
calendar_url = os.getenv("CALENDAR_URL")
calendar_id = os.getenv("CALENDAR_ID")
url = f"{calendar_url}{calendar_id}"
token = os.getenv("NOTION_TOKEN", "")
if not token:
    raise ValueError("NOTION_TOKEN не установлен или пуст.")
notion_version = "2022-02-22"
dt = datetime.strptime("2024-10-02", "%Y-%m-%d").replace(tzinfo=timezone.utc)

anounce_view = AnounceView()
create_ride = CreateRide()

get_route_id = GetRouteId(create_ride.ride_properties)
notion_parser = ParseNotion(
    url=url,
    token=token,
    notion_version=notion_version,
)
create_route = CreateRoute()
parse_route = ParseRouteData()

send_anounce = SendAnounce(
    anounce_bot=anounce_bot,
    anounce_view=anounce_view,
    create_ride=create_ride,
    notion_parser=notion_parser,
    create_route=create_route,
    parse_route=parse_route,
)

if __name__ == "__main__":
    send_anounce.send(date=dt)
