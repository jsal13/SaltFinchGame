"""
Generates a list of events with their details.

Each event has a name, description, type (positive, negative, neutral), and a dictionary of resources with their respective multipliers.
"""

from saltfinch.economy.economic_events import EconomicEvent
from saltfinch._data.economy.goods import GoodName

FOREST_EVENTS: list["EconomicEvent"] = [
    EconomicEvent(
        "Forest Fire",
        "A fire has damaged part of the nearby forest.",
        {GoodName.LUMBER.value: 1.5},
    ),
    EconomicEvent(
        "Animal Overpopulation",
        "The local wildlife is thriving, leading to overpopulation.",
        {
            GoodName.MEAT.value: 0.6,
        },
    ),
]
