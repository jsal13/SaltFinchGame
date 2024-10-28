from typing import Any

import pytest

from saltfinchgame.data_structures.ascii_map import MapASCII, MapLocation


def test_map_location_runs_with_defaults():
    assert MapLocation()


def test_map_location_runs_with_values():
    assert MapLocation(x=3, y=5)


def test_map_location_errors_with_negatives():
    with pytest.raises(ValueError, match=r".*must be >= 0.*"):
        assert MapLocation(x=-1, y=5)

    with pytest.raises(ValueError, match=r".*must be >= 0.*"):
        assert MapLocation(x=2, y=-6)

    with pytest.raises(ValueError, match=r".*must be >= 0.*"):
        assert MapLocation(x=-3, y=-5)


def test_map_location_initializes(ascii_map_values_fixture: dict[Any, Any]):
    map_ascii: MapASCII = MapASCII(
        width=ascii_map_values_fixture["Width"],
        height=ascii_map_values_fixture["Height"],
        symbols=ascii_map_values_fixture["Symbols"],
    )
    map_ascii._generate_map_grid_base_layer()

    assert map_ascii.map_grid is not None


def test_map_location__generate_area_locations_runs_with_towns(
    ascii_map_values_fixture, townlist_fixture
):
    map_ascii: MapASCII = MapASCII(
        width=ascii_map_values_fixture["Width"],
        height=ascii_map_values_fixture["Height"],
        symbols=ascii_map_values_fixture["Symbols"],
    )
    map_ascii._generate_map_grid_base_layer()
    map_ascii._generate_area_locations(areas=townlist_fixture)

    assert map_ascii.map_grid is not None


def test_map_location__generate_area_locations_runs_with_countries(
    ascii_map_values_fixture, countrylist_fixture
):
    map_ascii: MapASCII = MapASCII(
        width=ascii_map_values_fixture["Width"],
        height=ascii_map_values_fixture["Height"],
        symbols=ascii_map_values_fixture["Symbols"],
    )
    map_ascii._generate_map_grid_base_layer()
    map_ascii._generate_area_locations(areas=countrylist_fixture)

    assert map_ascii.map_grid is not None


def test_map_location__generate_area_locations_runs_with_nonarea(
    ascii_map_values_fixture, countrylist_fixture
):
    map_ascii: MapASCII = MapASCII(
        width=ascii_map_values_fixture["Width"],
        height=ascii_map_values_fixture["Height"],
        symbols=ascii_map_values_fixture["Symbols"],
    )
    map_ascii._generate_map_grid_base_layer()

    with pytest.raises(
        Exception, match=r"`areas` is not a `TownList` or `CountryList`."
    ):
        map_ascii._generate_area_locations(areas="")


# def _generate_area_locations(self, areas: CountryList | TownList) -> None:
#     """Generate town or country locations on the map."""
#     if self.map_grid is None:
#         msg: str = "`map_grid` has not been initialized."
#         raise Exception(msg)

#     for area in areas:
#         x, y = area.map_location

#         if isinstance(area, Town):
#             self.map_grid[y][x] = self.symbols["Town"]
#         elif isinstance(area, Country):
#             self.map_grid[y][x] = self.symbols["Country"]
#         else:
#             msg: str = "`area` is not a `Town` or `Country`."
#             raise Exception(msg)

#         for n, letter in enumerate(area.name.name):
#             self.map_grid[y + 1][x + n - 2] = letter
