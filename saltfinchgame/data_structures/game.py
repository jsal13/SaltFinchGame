from attrs import define

from saltfinchgame.data_structures.locations import CountryList, TownList
from saltfinchgame.data_structures.player import Player


@define()
class Game:
    """Game object."""

    player: Player
    countries: CountryList
    towns: TownList
