# Standard Library
import os
from datetime import datetime
from logging import getLogger

# Third Party Stuff
from dotenv import load_dotenv
from telebot import TeleBot

# My Stuff
from src.anounce.ride.abs import (
    AbstractCreateRide,
    AbstractRequestRide,
)
from src.anounce.route.abs import (
    AbstractCreateRoute,
    AbstractParseRoute,
)

from .abs import (
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
        parse_ride: AbstractRequestRide,
        create_route: AbstractCreateRoute,
        parse_route: AbstractParseRoute,
    ):
        self.anounce_bot = anounce_bot
        self.anounce_view = anounce_view
        self.create_ride = create_ride
        self.parse_ride = parse_ride
        self.create_route = create_route
        self.parse_route = parse_route
        self.logger = getLogger(__name__)

    def send(
        self,
        date: datetime,
    ) -> None:
        ride_properties = self.parse_ride.parse(date)
        ride = self.create_ride.create(ride_properties)
        response_route_properties = self.parse_route.parse(ride.route_id)
        ride.route = self.create_route.create_route(response_route_properties)
        self.logger.debug(f"ride.route: {ride.route}")
        message_text = self.anounce_view.get(ride)

        self.anounce_bot.send_message(
            chat_id=os.getenv("CHANNEL_ID", ""),
            text=message_text,
            parse_mode="HTML",
        )
