"""
This module defines a set of goods and their properties for a trading simulation.

The goods are represented by the `Good` class, which includes attributes such as
name, base price, volatility, and current price.

The `ALL_GOODS` dictionary contains all available goods, each represented by a
`Good` object. The goods are categorized based on the type of town they are
available in, such as forest, mountain, desert, and city.
"""

from enum import Enum

from saltfinch.economy.goods import Good  # type: ignore[import]


class GoodName(Enum):
    """
    Enum for the names of goods.

    This is used to ensure that the names of goods are consistent throughout the codebase.
    """

    WATER = "water"
    MEAT = "meat"
    LUMBER = "lumber"
    SALT = "salt"
    AMBER = "amber"

    def __iter__(self):
        """
        Iterate over the enum members.
        """
        return iter(self.__class__.__members__.values())


# Goods that are for survival in additionl to being traded.
GAMEPLAY_GOODS: dict[str, "Good"] = {
    GoodName.WATER.value: Good.create("Water", 4, 0.05),
    GoodName.MEAT.value: Good.create("Meat", 12, 0.25),
}

# Goods that are primarily used for trading.
TRADE_GOODS: dict[str, "Good"] = {
    GoodName.LUMBER.value: Good.create("Lumber", 35, 0.10),
    GoodName.SALT.value: Good.create("Salt", 30, 0.20),
    GoodName.AMBER.value: Good.create("Amber", 100, 0.30),
}

# All goods that are used for trading and survival.
ALL_GOODS = {**GAMEPLAY_GOODS, **TRADE_GOODS}

FOREST_TOWN_GOODS: list[str] = [
    GoodName.MEAT.value,
    GoodName.LUMBER.value,
    GoodName.WATER.value,
]

# MOUNTAIN_TOWN_GOODS: list[str] = [
#     "wheat",
#     "apples",
#     "cheese",
#     "chicken",
#     "fish",
#     "iron",
#     "tools",
# ]

# DESERT_TOWN_GOODS: list[str] = [
#     "wheat",
#     "apples",
#     "cheese",
#     "chicken",
#     "fish",
#     "salt",
#     "water",
# ]

# CITY_TOWN_GOODS: list[str] = [
#     "wheat",
#     "apples",
#     "cheese",
#     "chicken",
#     "fish",
#     "cloth",
#     "medicine",
# ]


def _generate_goods_dict_from_goods_list(
    goods_list: list[str],
) -> dict[str, "Good"]:
    """
    Generate a dictionary of goods based on the provided list of good names.

    The keys of the dictionary are the good names, and the values are the
    corresponding Good objects from the ALL_GOODS dictionary.
    """
    goods_dict: dict[str, "Good"] = {}
    for good_name in goods_list:
        goods_dict[good_name] = ALL_GOODS[good_name]
    return goods_dict


# Mapping of town types to their respective goods.
# This mapping is used to determine which goods are available in each town type.
# The keys are the town types, and the values are dictionaries of goods.
# where the keys are the good names and the values are the Good objects.
TOWN_GOODS_MAPPING: dict[str, dict[str, "Good"]] = {
    "forest": _generate_goods_dict_from_goods_list(goods_list=FOREST_TOWN_GOODS),
    # "mountain": _generate_goods_dict(goods_list=MOUNTAIN_TOWN_GOODS),
    # "desert": _generate_goods_dict(goods_list=DESERT_TOWN_GOODS),
    # "city": _generate_goods_dict(goods_list=CITY_TOWN_GOODS),
    "all": _generate_goods_dict_from_goods_list(goods_list=list(ALL_GOODS.keys())),
}
