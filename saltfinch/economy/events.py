
from attrs import define
from enum import Enum

class EconomicEventType(Enum):
    POSITIVE = 1
    NEGATIVE = 2
    NEUTRAL = 3

@define
class EconomicEvent:
    name: str
    description: str
    event_type: EconomicEventType
     # goods and their multiplier (above 1 for price increase, below 1 for decrease)
    affected_goods: dict[str, float] 


