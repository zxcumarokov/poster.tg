# My Stuff
from src.anounce.create_route import CreateRoute


def test_create_route() -> None:
    # Хардкодим JSON данные прямо в коде как словарь
    route_properties = {
        "Маршрут": {"url": "https://go.2gis.com/v3o2"},
        "Дистанция": {"number": 9.4},
        "Набор, м": {"number": 1172},
        "кофе брейк ": {"url": "https://go.2gis.com/v3"},
        "сегмент дня ": {"url": "https://go.2gis.com/v3o"},
        "Место старта ": {"url": "https://go.2gis.com/v3o2e"},
        "URL": {"url": "https://www.strava.com/routes/3277971384710128806"},
        "Name": {"title": [{"text": {"content": "Ледяной грот Дельфин"}}]},
    }

    create_route = CreateRoute()

    # Передаем словарь в метод create_route
    route = create_route.create_route(route_properties)

    # Проверяем, что объект route был создан
    assert route
