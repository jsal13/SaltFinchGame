from saltfinchgame.constants import ASCII_MAP_VALUES
from saltfinchgame.data_structures.ascii_map import MapASCII
from saltfinchgame.data_structures.locations import TownList
from saltfinchgame.ui.generate_map_str import (
    print_map_as_formatted_str,
    return_map_str,
)


def print_map_of_country(townlist_for_country: TownList) -> None:
    """Print the map of a country."""
    ma = MapASCII(
        width=ASCII_MAP_VALUES["Width"],
        height=ASCII_MAP_VALUES["Height"],
        symbols=ASCII_MAP_VALUES["Symbols"],
    )
    ma._generate_map_grid_base_layer()
    ma._generate_area_locations(areas=townlist_for_country)
    _map = return_map_str(ma.map_grid)
    print_map_as_formatted_str(_map)
