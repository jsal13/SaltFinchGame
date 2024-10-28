from saltfinchgame.data_structures.ascii_map import MapLocation
from saltfinchgame.data_structures.locations import (
    Area,
    Country,
    CountryList,
    Description,
    Town,
    TownList,
)


def test_description_initializes():
    Description(weather="Good", resources="Good", misc_facts="Good, also.")


def test_area_initializes():
    Area(name="Testsss", description="", map_location=MapLocation(x=1, y=2))


def test_town_initializes(town_fixture):
    assert town_fixture


def test_townlist_initializes(townlist_fixture):
    assert townlist_fixture


def test_country_initializes(country_fixture):
    assert country_fixture


def test_countrylist_initializes(countrylist_fixture):
    assert countrylist_fixture
