"""
Creates EconomicEvent objects that represent events affecting the economy.
These events can affect the prices of goods in a town.
"""

from typing import TYPE_CHECKING

from attrs import define


if TYPE_CHECKING:
    from saltfinch._data.economy.goods import GoodName


@define
class EconomicEvent:
    """
    Represents an economic event that can affect the prices of goods in a town.
    """

    name: str
    description: str
    affected_goods: dict[str, float]
