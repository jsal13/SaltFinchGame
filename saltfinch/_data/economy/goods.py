"""
This module defines a set of goods and their properties for a trading simulation.

The goods are represented by the `Good` class, which includes attributes such as
name, base price, volatility, and current price.

The `ALL_GOODS` dictionary contains all available goods, each represented by a
`Good` object. The goods are categorized based on the type of town they are
available in, such as forest, mountain, desert, and city.
"""

from saltfinch.economy.goods import Good  # type: ignore[import]

ALL_GOODS: dict[str, "Good"] = {
    "wheat": Good.create("Wheat", 10.0, 0.15),
    "apples": Good.create("Apples", 12.0, 0.25),
    "cheese": Good.create("Cheese", 15.0, 0.15),
    "chicken": Good.create("Chicken", 20.0, 0.15),
    "fish": Good.create("Fish", 20.0, 0.10),
    "wool": Good.create("Wool", 25.0, 0.20),
    "lumber": Good.create("Lumber", 35.0, 0.10),
    "iron": Good.create("Iron", 45.0, 0.15),
    "cloth": Good.create("Cloth", 18.0, 0.15),
    "medicine": Good.create("Medicine", 50.0, 0.25),
    "tools": Good.create("Tools", 40.0, 0.10),
    "salt": Good.create("Salt", 30.0, 0.20),
    "water": Good.create("Water", 4.0, 0.05),
}

FOREST_TOWN_GOODS: list[str] = [
    "apples",
    "cheese",
    "lumber",
]

MOUNTAIN_TOWN_GOODS: list[str] = [
    "wheat",
    "apples",
    "cheese",
    "chicken",
    "fish",
    "iron",
    "tools",
]

DESERT_TOWN_GOODS: list[str] = [
    "wheat",
    "apples",
    "cheese",
    "chicken",
    "fish",
    "salt",
    "water",
]

CITY_TOWN_GOODS: list[str] = [
    "wheat",
    "apples",
    "cheese",
    "chicken",
    "fish",
    "cloth",
    "medicine",
]


def _generate_goods_dict(goods_list: list[str]) -> dict[str, "Good"]:
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
    "forest": _generate_goods_dict(goods_list=FOREST_TOWN_GOODS),
    "mountain": _generate_goods_dict(goods_list=MOUNTAIN_TOWN_GOODS),
    "desert": _generate_goods_dict(goods_list=DESERT_TOWN_GOODS),
    "city": _generate_goods_dict(goods_list=CITY_TOWN_GOODS),
    "all": _generate_goods_dict(goods_list=list(ALL_GOODS.keys())),
}
