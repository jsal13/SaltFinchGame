from typing import TYPE_CHECKING

from attrs import define

if TYPE_CHECKING:
    from saltfinchgame.data_structures.items import ItemsList


@define()
class Trader:
    """Parent class for traders."""

    name: str
    items: "ItemsList"
