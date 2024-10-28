from saltfinchgame.data_structures.ascii_map import MapLocation
from saltfinchgame.data_structures.locations import (
    Area,
    Description,
)


def test_description_initializes():
    Description(weather="Good", resources="Good", misc_facts="Good, also.")


def test_area_initializes():
    Area(name="Testsss", description="", map_location=MapLocation(x=1, y=2))


def test_maplocation_iterates():
    x, y = MapLocation(x=1, y=1)
    assert x == y


def test_town_initializes(town_fixture):
    assert town_fixture


def test_townlist_initializes(townlist_fixture):
    assert townlist_fixture


def test_townlist_get_by_name_runs(townlist_fixture):
    assert townlist_fixture.get_by_name("Testville")


def test_country_initializes(country_fixture):
    assert country_fixture


def test_countrylist_initializes(countrylist_fixture):
    assert countrylist_fixture


def test_countrylist_get_by_name_runs(countrylist_fixture):
    assert countrylist_fixture.get_by_name("Testvia")


def test_countrylist_iter_works(countrylist_fixture):
    assert list(countrylist_fixture)
