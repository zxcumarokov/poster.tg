# Standard Library
from datetime import (
    datetime,
    timezone,
)

# My Stuff
from src.anounce.abcview import AbstractViev

TYPE_OF_TRAINING = "СТАНОК!!!"
WORKOUT_APP = "ZWIFT"
TRAINING_TITLE = "Peak performance"
DISTANCE = "46км/726м"
POWER = "2 вт/кг"
PAYSER = "Пейсер - @sumarokov_cyclist"
CHANNEL = "Канал голосового общения: @roadbikealmaty"
CONDITIONS = """
        Для участия необходимо:
        ⁃ установить мобильное приложение Zwift Companion
        ⁃ Вступить в клуб 700c
        ⁃ Открыть страницу события 👆
        ⁃ Нажать + напротив своей категории (A, B, C, D, E)
        ⁃ Зайти в Zwift за 10 минут до начала
        ⁃ Проверить соединение датчиков заблаговременно
        ⁃ Войти в голосовой чат 700с
"""
CALENDAR = "📅 Календарь тренировок"
MANUAL_FOR_PAYSER = "👑 Инструкция для пейсера"
GEST_URES = "👇 Жесты в группе"
POSTSCRIPTUM = " P.S.: Плюсы и фотки в комменты пл"

ROUTE_URL = "https://strava.com"


class AnounceView(AbstractViev):
    def get(self) -> str:
        current_time_utc = datetime.now(timezone.utc)
        formatted_time_utc = current_time_utc.strftime("%Y-%m-%d %H:%M")

        message_text = (
            f"{formatted_time_utc}\n\n"
            f"{TYPE_OF_TRAINING}\n\n"
            f"{WORKOUT_APP}: {TRAINING_TITLE}\n"
            f"{DISTANCE}\n\n"
            f"Мощность: {POWER}\n"
            f"{PAYSER}\n"
            f"{CHANNEL}\n\n"
            f"{CONDITIONS}\n"
            f"{CALENDAR}\n"
            f"{MANUAL_FOR_PAYSER}\n"
            f"{GEST_URES}\n\n"
            f"{POSTSCRIPTUM}\n\n"
            f'Маршрут: <a href="{ROUTE_URL}">здесь</a>\n'
        )
        return message_text
