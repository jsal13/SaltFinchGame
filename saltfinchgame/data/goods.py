from saltfinchgame.data.goods_names import GoodsName
from saltfinchgame.data_structures.goods import BasicGoods, LuxuryGoods

BASIC_GOODS: list[BasicGoods] = [
    BasicGoods(
        name=GoodsName.WATER, description="Clear liquid. Required for survival."
    ),
    BasicGoods(
        name=GoodsName.SLABS_OF_MEAT, description="Basic food. Required for survival."
    ),
    BasicGoods(
        name=GoodsName.PACK_OF_VEGETABLES,
        description="Basic food. Required for survival.",
    ),
]

LUXURY_GOODS: list[LuxuryGoods] = [
    LuxuryGoods(
        name=GoodsName.CARPET,
        description="Woven ornamental item.  Heavy, but valuable.",
    ),
    LuxuryGoods(
        name=GoodsName.SALT,
        description="Tiny white crystals, useful for curing meats and seasoning.",
    ),
    LuxuryGoods(
        name=GoodsName.DATES, description="Sweet, candy-like fruits.  High in fiber."
    ),
]
