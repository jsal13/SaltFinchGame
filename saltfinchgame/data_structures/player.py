from attrs import define, field

from saltfinchgame.constants import STARTING_VALUES
from saltfinchgame.data_structures.goods import Goods


@define()
class Player:
    """Player object."""

    name: str = field(default=STARTING_VALUES["Name"])
    health: int = field(default=STARTING_VALUES["Health"])
    silver: int = field(default=STARTING_VALUES["Silver"])
    goods: list["Goods"]
