from saltfinch.data.economy.goods import TOWN_GOODS_MAPPING
from saltfinch.data.economy.events import ALL_EVENTS
from saltfinch.economy.town_economies import TownEconomy

TOWN_ECONOMIES = {
    "forest": TownEconomy(goods=TOWN_GOODS_MAPPING["forest"], events=ALL_EVENTS)
}
