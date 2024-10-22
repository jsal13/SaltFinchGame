from attrs import define


@define()
class Goods:
    """Parent class for goods."""

    name: str
    description: str
    default_buy_price: int
    default_sell_price: int


@define()
class BasicGoods(Goods):
    """Basic Goods."""


@define()
class LuxuryGoods(Goods):
    """Goods which are not usable by the party (for selling only)."""
