from typing import TYPE_CHECKING

from attrs import define

if TYPE_CHECKING:
    from saltfinchgame.data.goods_names import GoodsName


@define()
class Goods:
    """Parent class for goods."""

    name: "GoodsName"
    description: str
    default_buy_price: int
    default_sell_price: int


@define()
class BasicGoods(Goods):
    """Basic Goods."""


@define()
class LuxuryGoods(Goods):
    """Goods which are not usable by the party (for selling only)."""
