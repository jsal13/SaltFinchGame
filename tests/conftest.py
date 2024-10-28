from typing import Any

import pytest

from saltfinchgame.data_structures.ascii_map import MapLocation
from saltfinchgame.data_structures.items import Item, ItemList
from saltfinchgame.data_structures.locations import Country, CountryList, Town, TownList
from saltfinchgame.data_structures.player import Player


@pytest.fixture
def ascii_map_values_fixture() -> dict[Any, Any]:
    return {
        "Width": 50,
        "Height": 20,
        "Symbols": {"Town": "#", "Player": "@", "Background": ".", "Country": "%"},
    }


@pytest.fixture
def player_fixture() -> Player:
    return Player(name="Tests MacTests", health=100, silver=10, items=[])


@pytest.fixture
def town_fixture() -> Town:
    return Town(
        name="Testville",
        description="",
        map_location=MapLocation(x=1, y=2),
        country="Testvia",
        items_selling=None,
        items_buying=None,
        inn_cost=10,
    )


@pytest.fixture
def townlist_fixture() -> TownList:
    town_0 = Town(
        name="Testville",
        description="",
        map_location=MapLocation(x=1, y=2),
        country="Testvia",
        items_selling=None,
        items_buying=None,
        inn_cost=10,
    )
    town_1 = Town(
        name="Testberg",
        description="",
        map_location=MapLocation(x=2, y=3),
        country="Testvia",
        items_selling=None,
        items_buying=None,
        inn_cost=10,
    )
    town_2 = Town(
        name="Tests Grove",
        description="",
        map_location=MapLocation(x=3, y=4),
        country="Republic of Tests",
        items_selling=None,
        items_buying=None,
        inn_cost=10,
    )
    town_3 = Town(
        name="Test Hills",
        description="",
        map_location=MapLocation(x=4, y=5),
        country="Republic of Tests",
        items_selling=None,
        items_buying=None,
        inn_cost=10,
    )
    return TownList(towns=[town_0, town_1, town_2, town_3])


@pytest.fixture
def country_fixture(townlist_fixture) -> Country:
    return Country(
        name="Testvia",
        description="",
        map_location=MapLocation(1, 1),
        towns=[town for town in townlist_fixture if town.country == "Testvia"],
    )


@pytest.fixture
def countrylist_fixture(townlist_fixture) -> CountryList:
    country_0 = Country(
        name="Testvia",
        description="",
        map_location=MapLocation(1, 1),
        towns=[town for town in townlist_fixture if town.country == "Testvia"],
    )
    country_1 = Country(
        name="Republic of Tests",
        description="",
        map_location=MapLocation(1, 1),
        towns=[
            town for town in townlist_fixture if town.country == "Republic of Tests"
        ],
    )
    return CountryList(countries=[country_0, country_1])


@pytest.fixture
def item_fixture() -> Item:
    return Item(
        name="Test Item",
        buy_price=10,
        sell_price=20,
    )


@pytest.fixture
def itemlist_fixture() -> Item:
    item_0 = Item(
        name="Test Item",
        buy_price=10,
        sell_price=20,
    )
    item_1 = Item(
        name="Test Item 2",
        buy_price=20,
        sell_price=50,
    )
    return ItemList(items=[item_0, item_1])
