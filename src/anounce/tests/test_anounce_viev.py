# My Stuff
from src.anounce.anounce_view import AnounceView
from src.models.notion_calendar.calendar import Ride
from src.models.notion_calendar.route import Route


def test_view() -> None:
    ride = Ride(
        training_name="training_name",
        date="date",
        type_of_training="type_of_training",
        workout_app="workout_app",
        power="power",
        payser="payser",
        voice_chanel="voice_chanel",
        condition="condition",
        manual_for_payser="manual_for_payser",
        gest_ures="gest_ures",
        post_scriptum="post_scriptum",
        route_id="route_id",
    )

    roate = Route(
        distance=22,
        set_count=52,
        route_name="route_name",
        coffee_break="coffee_break",
        day_segment="day_segment",
        start_place="start_place",
    )

    anounce_view = AnounceView()
    message_text = anounce_view.get(ride, roate)
    assert message_text
