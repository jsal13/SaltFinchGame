from attrs import define, field

from saltfinchgame.constants import STARTING_VALUES
from saltfinchgame.data_structures.locations import Country, Town


@define()
class Game:
    """Game object."""

    is_alive: bool = field(default=True)
    current_town: "Town" = field(default=STARTING_VALUES["Town"])
    current_country: "Country" = field(default=STARTING_VALUES["Country"])
