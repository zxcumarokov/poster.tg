# Third Party Stuff
from pydantic import BaseModel

from .route import Route


class Ride(BaseModel):
    training_name: str
    date: str
    type_of_training: str
    workout_app: str
    power: str
    payser: str
    voice_chanel: str
    condition: str
    manual_for_payser: str
    gest_ures: str
    post_scriptum: str
    route_id: str
    route: Route
