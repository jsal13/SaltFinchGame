from attrs import define, field

from saltfinchgame.data_structures.goods import GoodsList


@define()
class Trader:
    """Parent class for traders."""

    name: str = field(default="Trade Armin")
    goods: GoodsList
