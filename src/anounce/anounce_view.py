# Standard Library
from datetime import (
    datetime,
    timezone,
)

# My Stuff
from src.models.notion_calendar.calendar import Ride
from src.models.notion_calendar.route import Route  # Не забудьте импортировать Route

from .abs import AbstractView


class AnounceView(AbstractView):
    def __init__(self):
        pass

    def get(self, ride: Ride, route: Route) -> str:
        current_time_utc = datetime.now(timezone.utc)
        formatted_time_utc = current_time_utc.strftime("%Y-%m-%d %H:%M")

        message_text = (
            f"{formatted_time_utc}\n\n"
            f"{ride.type_of_training}\n\n"
            f"{ride.workout_app}: {ride.training_name}\n"
            f"Расстояние: {route.distance} км\n"
            f"Количество наборов: {route.set_count}\n"
            f"Кофе-брейк: {route.coffee_break}\n"
            f"Сегмент дня: {route.day_segment}\n"
            f"Место старта: {route.start_place}\n\n"
            f"{ride.voice_chanel}\n\n"
            f"{ride.condition}\n"
            f"{ride.manual_for_payser}\n"
            f"{ride.gest_ures}\n\n"
            f"{ride.post_scriptum}\n\n"
            f'Маршрут: <a href="{ride.route_id}">здесь</a>\n'
        )

        return message_text
