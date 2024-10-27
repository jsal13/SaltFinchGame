from saltfinchgame.data.countries import COUNTRIES, CountryName
from saltfinchgame.data_structures.ascii_map import MapASCII
from saltfinchgame.utils.generate_map_str import (
    print_map_as_formatted_str,
    return_map_str,
)


def print_map_of_country(country_name: CountryName) -> None:
    """Print the map of a country."""
    towns_in_country = COUNTRIES.get_by_name(country_name).towns
    ma = MapASCII()
    ma._generate_map_grid_base_layer()
    ma._generate_area_locations(areas=towns_in_country)
    _map = return_map_str(ma.map_grid)
    print_map_as_formatted_str(_map)
