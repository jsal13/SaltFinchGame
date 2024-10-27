from attrs import define, field

# from saltfinchgame.constants import STARTING_VALUES
# from saltfinchgame.data_structures.locations import Country, Town
from saltfinchgame.data.countries import COUNTRIES
from saltfinchgame.data.towns import TOWNS
from saltfinchgame.data_structures.locations import CountryList, TownList
from saltfinchgame.data_structures.player import Player


@define()
class Game:
    """Game object."""

    is_alive: bool = field(default=True)

    player: Player = field(default=Player(goods=""))
    countries: CountryList = field(default=COUNTRIES)
    towns: TownList = field(default=TOWNS)


g = Game()
