# My Stuff
from src.anounce.ride.implementations import CreateRide


def test_create_ride() -> None:
    # Хардкодим JSON данные прямо в коде как словарь
    ride_properties = {
        "Маршрут": {"relation": [{"id": "ff3ec128-950f-4723-a8a5-6f0e53bfa568"}]},
        "Date": {"date": {"start": "2024-10-02"}},
        "voice_channel": {"url": "@roadbikealmaty"},
        "Pacer": {"people": [{"name": "ivan sumarokov"}]},
        "мощьность": {"select": {"name": "2вт/кг"}},
        "post_scriptum": {
            "rich_text": [{"text": {"content": "Плюсы и фотки в комменты пл"}}]
        },
        "application": {"select": {"name": "звифт"}},
        "Тип тренировки": {"select": {"name": "станок"}},
        "conditions": {
            "rich_text": [
                {"text": {"content": "установить мобильное приложение Zwift Companion"}}
            ]
        },
        "gest ures": {
            "url": "https://chrome-earl-520.notion.site/415c58ef620640bb80698e588b6a34c5"
        },
        "manual_for_payser": {
            "url": "https://chrome-earl-520.notion.site/95c5299e58894f12b7953568f8e55e44"
        },
        "Name": {"title": [{"text": {"content": "First workout"}}]},
    }

    create_ride = CreateRide()

    # Передаем словарь в метод create_ride
    ride = create_ride.create(ride_properties)

    # Проверяем, что объект ride был создан
    assert ride
