# Standard Library
import os
from datetime import (
    datetime,
    timezone,
)
from logging import basicConfig

# Third Party Stuff
from dotenv import load_dotenv
from telebot import TeleBot

# My Stuff
from src.anounce.anounce_view import AnounceView
from src.anounce.ride.implementations import (
    CreateRide,
    RequestRide,
)
from src.anounce.route.implementations import (
    CreateRoute,
    ParseRouteData,
)

from .send_anounce import SendAnounce

load_dotenv()
anounce_bot = TeleBot(os.getenv("BOT_TOKEN", ""))
if not anounce_bot:
    raise ValueError("BOT_TOKEN не установлен или пуст.")
calendar_url = os.getenv("CALENDAR_URL")
calendar_id = os.getenv("CALENDAR_ID")
url = f"{calendar_url}{calendar_id}"
token = os.getenv("NOTION_TOKEN")
if not token:
    raise ValueError("NOTION_TOKEN не установлен или пуст.")
notion_version = "2022-02-22"
dt = datetime.strptime("2024-10-02", "%Y-%m-%d").replace(tzinfo=timezone.utc)
notion_token = os.getenv("NOTION_TOKEN")
if not notion_token:
    raise ValueError("NOTION_TOKEN не установлен или пуст.")
notion_base_url = os.getenv("NOTION_BASE_URL")
if not notion_base_url:
    raise ValueError("NOTION_BASE_URL не установлен или пуст.")
anounce_view = AnounceView()
create_ride = CreateRide()

parse_ride = RequestRide(
    url=url,
    token=token,
    notion_version=notion_version,
)
create_route = CreateRoute()
parse_route = ParseRouteData(notion_base_url=notion_base_url, notion_token=notion_token)

send_anounce = SendAnounce(
    anounce_bot=anounce_bot,
    anounce_view=anounce_view,
    create_ride=create_ride,
    parse_ride=parse_ride,
    create_route=create_route,
    parse_route=parse_route,
)

if __name__ == "__main__":
    basicConfig(
        level="DEBUG",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    send_anounce.send(date=dt)
