# My Stuf
# Standard Library
from os import getenv

# My Stuff
from src.anounce.parseroute import NotionDataFetcher
from src.models.bot import IView


class AnounceView(IView):
    def __init__(self, notion_parser: NotionDataFetcher,):
        self.notion_parser = notion_parser

    def get(self):
        
        # Инициализируем fetcher и получаем ссылки
        links = self.notion_parser.fetch_data()  # Получаем список ссылок

        # Проверяем, есть ли ссылки
        event_link = links[0] if links else "#"  # Используем первую ссылку или заглушку

        result = f"""
        <b>10 сентября 8:00</b>

        <b>СТАНОК!!!</b>

        <a href="{event_link}"><b>Zwift: Peak performance</b></a>
        46км/726м

        Мощность 2 вт/кг

        Пейсер - <a href="https://t.me/sumarokov_cyclist">@sumarokov_cyclist</a>
        Канал голосового общения: <a href="https://t.me/roadbikealmaty">@roadbikealmaty</a>

        <b>Для участия необходимо:</b>
        ⁃ установить мобильное приложение <a href="https://apps.apple.com/kz/app/zwift-companion/id934083691">Zwift Companion</a>
        ⁃ <a href="https://www.zwift.com/events/view/4502381">Вступить в клуб 700c</a>
        ⁃ Открыть страницу события 👆
        ⁃ Нажать + напротив своей категории (A, B, C, D, E)
        ⁃ Зайти в Zwift за 10 минут до начала
        ⁃ Проверить соединение датчиков заблаговременно
        ⁃ Войти в голосовой чат 700с

        <a href="https://chrome-earl-520.notion.site/a3b9f73785be4b7d8ac4ebc65bd57439?v=105442eaff29413ba2fa2769c5965e9d&pvs=4">📅 Календарь тренировок</a>
        <a href="https://chrome-earl-520.notion.site/95c5299e58894f12b7953568f8e55e44?pvs=4">👑 Инструкция для пейсера</a>
        <a href="https://chrome-earl-520.notion.site/415c58ef620640bb80698e588b6a34c5?pvs=4">👇 Жесты в группе</a>

        <i>P.S.: Плюсы и фотки в комменты пл</i>

        <b>Нажали на кнопку "Увидел": 0</b>
        """
        return result
    def create_message(self):
        message = self.get()
        return message 
