# Third Party Stuff
from pydantic import BaseModel


class ParseResult(BaseModel):
    route_url: str
