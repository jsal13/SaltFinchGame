from typing import TYPE_CHECKING, Optional

from attrs import define

if TYPE_CHECKING:
    from saltfinchgame.data_structures.ascii_map import MapLocation
    from saltfinchgame.data_structures.items import ItemList


@define()
class Description:
    """Description of an Area."""

    weather: str | None
    resources: str | None
    misc_facts: str | None


@define()
class Area:
    """Parent class for cities, towns, countries, etc."""

    name: str
    description: Description | str
    map_location: "MapLocation"


@define()
class Town(Area):
    """Represents a Town/City."""

    country: str
    item_list: Optional["ItemList"]
    inn_cost: int


@define()
class TownList:
    """Represents a list of towns."""

    towns: list[Town]

    def __iter__(self):
        yield from self.towns

    def get_by_name(self, name: str) -> Town:
        """Get town by name."""
        # There should only be one element here.
        return next(town for town in self.towns if town.name == name)


@define()
class Country(Area):
    """Represents a Country."""

    towns: TownList


@define()
class CountryList:
    """Represents a list of countries."""

    countries: list[Country]

    def __iter__(self):
        yield from self.countries

    def get_by_name(self, name: str) -> Country:
        """Get town by name."""
        # There should only be one element here.
        return next(country for country in self.countries if country.name == name)
