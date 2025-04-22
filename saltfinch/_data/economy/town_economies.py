from saltfinch._data.economy.goods import TOWN_GOODS_MAPPING
from saltfinch._data.economy.economic_events import ALL_EVENTS
from saltfinch.economy.town_economies import TownEconomy

TOWN_ECONOMIES = {
    "forest": TownEconomy(goods=TOWN_GOODS_MAPPING["forest"], economic_events=ALL_EVENTS)
}
