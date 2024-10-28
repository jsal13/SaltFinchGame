from typing import TYPE_CHECKING

from attrs import define

if TYPE_CHECKING:
    from saltfinchgame.data_structures.items import Items


@define()
class Player:
    """Player object."""

    name: str
    health: int
    silver: int
    items: list["Items"]
