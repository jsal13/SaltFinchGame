from enum import Enum, auto

from saltfinchgame.data_structures.goods import BasicGoods, LuxuryGoods


class GoodsName(Enum):
    """Name of good."""

    WATER = auto()
    PACK_OF_VEGETABLES = auto()
    SLABS_OF_MEAT = auto()
    SALT = auto()
    CARPET = auto()
    DATES = auto()


BASIC_GOODS: dict["GoodsName":"BasicGoods"] = {
    GoodsName.WATER: BasicGoods(
        name="Water", description="Clear liquid. Required for survival."
    ),
    GoodsName.SLABS_OF_MEAT: BasicGoods(
        name="Slabs of Meat", description="Basic food. Required for survival."
    ),
    GoodsName.PACK_OF_VEGETABLES: BasicGoods(
        name="Pack of Vegetables", description="Basic food. Required for survival."
    ),
}

LUXURY_GOODS: dict["GoodsName":"LuxuryGoods"] = {
    GoodsName.CARPET: LuxuryGoods(
        name="Carpet", description="Woven ornamental item.  Heavy, but valuable."
    ),
    GoodsName.SALT: LuxuryGoods(
        name="Salt",
        description="Tiny white crystals, useful for curing meats and seasoning.",
    ),
    GoodsName.DATES: LuxuryGoods(
        name="Dates", description="Sweet, candy-like fruits.  High in fiber."
    ),
}
