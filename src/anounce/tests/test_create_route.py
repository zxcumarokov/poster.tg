# My Stuff
from src.anounce.route.implementations import CreateRoute


def test_create_route() -> None:
    # Адаптируем JSON данные, чтобы они соответствовали ожидаемым в классе CreateRoute
    route_properties = {
        "сегмент дня ": {"url": "сегмент 1"},
        "Место старта ": {"url": "Точка старта"},
        "Набор, м": {"number": 1172},
        "кофе брейк ": {"url": "кафе на трассе"},
        "Дистанция": {"number": 9.4},
        "Name": {"title": [{"text": {"content": "Ледяной грот Дельфин"}}]},
    }

    create_route = CreateRoute()

    # Передаем словарь в метод create_route
    route = create_route.create_route(route_properties)
    assert route
