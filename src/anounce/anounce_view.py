# Standard Library
from datetime import (
    datetime,
    timezone,
)

# My Stuff
from src.anounce.ride import Ride

from .abs import AbstractView


class AnounceViewNoRouteError(ValueError):
    pass


class AnounceView(AbstractView):
    def get(self, ride: Ride) -> str:
        current_time_utc = datetime.now(timezone.utc)
        formatted_time_utc = current_time_utc.strftime("%Y-%m-%d %H:%M")
        if not ride.route:
            raise AnounceViewNoRouteError("Route not found")

        message_text = (
            f"{formatted_time_utc}\n\n"
            f"Тип тренировки: {ride.type_of_training}\n\n"
            f"Название тренировки: {ride.training_name}\n"
            f"Приложение: {ride.workout_app}: \n"
            f"Расстояние: {self._prepare_text(ride.route.distance)} км\n"
            f"Набор: {self._prepare_text(ride.route.climbing)}\n"
            f"Кофе-брейк: {self._prepare_text(ride.route.coffee_break)}\n"
            f"Сегмент дня: {self._prepare_text(ride.route.day_segment)}\n"
            f"Место старта: {self._prepare_text(ride.route.start_place)}\n\n"
            f"Голосовой канал: {ride.voice_chanel}\n\n"
            f"Описание условий: {ride.condition}\n"
            f"Мануал{ride.manual_for_payser}\n"
            f"Жесты: {ride.gest_ures}\n\n"
            f"PS:{ride.post_scriptum}\n\n"
            f'Маршрут: <a href="{ride.route_id}">здесь</a>\n'
        )

        return message_text

    def _prepare_text(self, data: str | float | None) -> str:
        if not data:
            return "-"
        if isinstance(data, float):
            return str(round(data, 2))
        if isinstance(data, str):
            return data.replace("None", "-")
        return str(data)
