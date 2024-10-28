from saltfinchgame.data.locations import TownList
from saltfinchgame.data_structures.ascii_map import MapASCII
from saltfinchgame.ui.generate_map_str import (
    print_map_as_formatted_str,
    return_map_str,
)


def print_map_of_country(towns_in_country_names: TownList) -> None:
    """Print the map of a country."""
    towns_in_country = [town.name for town in towns_in_country_names]
    ma = MapASCII()
    ma._generate_map_grid_base_layer()
    ma._generate_area_locations(areas=towns_in_country)
    _map = return_map_str(ma.map_grid)
    print_map_as_formatted_str(_map)
