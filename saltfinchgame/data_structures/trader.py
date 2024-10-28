from typing import TYPE_CHECKING

from attrs import define, field

if TYPE_CHECKING:
    from saltfinchgame.data_structures.items import ItemsList


@define()
class Trader:
    """Parent class for traders."""

    name: str = field(default="Trade Armin")
    items: ItemsList
