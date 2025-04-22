
from attrs import define
from enum import Enum

class EventType(Enum):
    POSITIVE = 1
    NEGATIVE = 2
    NEUTRAL = 3

@define
class Event:
    name: str
    description: str
    event_type: EventType
     # goods and their multiplier (above 1 for price increase, below 1 for decrease)
    affected_goods: dict[str, float] 


