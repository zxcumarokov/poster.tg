# Standard Library
import os
from datetime import datetime

# Third Party Stuff
from dotenv import load_dotenv
from telebot import TeleBot

from .abs import (
    AbstractCreateRide,
    AbstractCreateRoute,
    AbstractParseNotion,
    AbstractParseRoute,
    AbstractSend,
    AbstractView,
)

load_dotenv()

chat_id = os.getenv("CHANNEL_ID", "")
if not chat_id:
    raise ValueError("CHANNEL_ID не установлен или пуст.")


class SendAnounce(AbstractSend):
    def __init__(
        self,
        anounce_bot: TeleBot,
        anounce_view: AbstractView,
        create_ride: AbstractCreateRide,
        notion_parser: AbstractParseNotion,
        create_route: AbstractCreateRoute,
        parse_route: AbstractParseRoute,
    ):
        self.anounce_bot = anounce_bot
        self.anounce_view = anounce_view
        self.create_ride = create_ride
        self.notion_parser = notion_parser
        self.create_route = create_route
        self.parse_route = parse_route

    def send(
        self,
        date: datetime,
    ) -> None:
        ride_properties = self.notion_parser.parse(date)
        ride = self.create_ride.create_ride(ride_properties)
        response_route_properties = self.parse_route.parse(ride.route_id)
        route = self.create_route.create_route(response_route_properties)
        message_text = self.anounce_view.get(ride, route)

        self.anounce_bot.send_message(
            chat_id=os.getenv("CHANNEL_ID", ""),
            text=message_text,
            parse_mode="HTML",
        )
