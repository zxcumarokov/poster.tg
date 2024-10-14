# Standard Library

# My Stuff
from src.models.notion_calendar.calendar import Ride

from .abs import AbstractCreateRide


class CreateRide(AbstractCreateRide):
    def create_ride(self, ride_properties: dict) -> Ride:
        _type_of_training = ride_properties["Тип тренировки"]["select"]["name"]
        _date = ride_properties["Date"]["date"]["start"]
        _route_id = ride_properties["Маршрут"]["relation"][0]["id"]
        _voice_channel = ride_properties["voice_channel"]["url"]
        _pacer = ride_properties["Pacer"]["people"][0]["name"]
        _power = ride_properties["мощьность"]["select"]["name"]

        _post_scriptum = (
            ride_properties["post_scriptum"]["rich_text"][0]["text"]["content"]
            if ride_properties["post_scriptum"]["rich_text"]
            else ""
        )
        _workout_app = ride_properties["application"]["select"]["name"]

        _condition = (
            ride_properties["conditions"]["rich_text"][0]["text"]["content"]
            if ride_properties["conditions"]["rich_text"]
            else ""
        )

        _gestures = ride_properties["gest ures"]["url"]
        _manual_for_payser = ride_properties["manual_for_payser"]["url"]
        _name_workout = ride_properties["Name"]["title"][0]["text"]["content"]

        _ride = Ride(
            training_name=_name_workout,
            date=_date,
            type_of_training=_type_of_training,
            workout_app=_workout_app,
            power=_power,
            payser=_pacer,
            voice_chanel=_voice_channel,
            condition=_condition,
            manual_for_payser=_manual_for_payser,
            gest_ures=_gestures,
            post_scriptum=_post_scriptum,
            route_id=_route_id,
        )
        return _ride
