from dataclasses import dataclass
from .event_base import EventBase

@dataclass
class PersonBase:
    name: str
    events: list[EventBase]
