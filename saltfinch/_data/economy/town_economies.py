"""
Defines the town economies for the game.

This module contains the `TOWN_ECONOMIES` dictionary, which maps town
types to their respective economies. Each town economy is represented
by the `TownEconomy` class, which includes information about the goods
available in that town and the economic events that can occur.
"""

from saltfinch._data.economy.goods import TOWN_GOODS_MAPPING
from saltfinch._data.economy.economic_events import FOREST_EVENTS
from saltfinch.economy.town_economies import TownEconomy

TOWN_ECONOMIES = {
    "forest": TownEconomy(
        goods=TOWN_GOODS_MAPPING["forest"], economic_events=FOREST_EVENTS
    ),
}
