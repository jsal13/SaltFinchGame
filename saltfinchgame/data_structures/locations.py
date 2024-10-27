from attrs import define

from saltfinchgame.data.location_attributes import Biome, MapLocation, Size
from saltfinchgame.data.location_names import CountryName, TownName


@define()
class Description:
    """Description of an Area."""

    size: Size
    biomes: list[Biome] | None
    weather: str | None
    resources: str | None
    misc_facts: str | None


@define()
class Area:
    """Parent class for cities, towns, countries, etc."""

    name: TownName | CountryName
    description: Description | str
    map_location: MapLocation


@define()
class Town(Area):
    """Represents a Town/City."""

    country: "CountryName"
    goods_selling: str
    goods_buying: str
    inn_cost: int


@define()
class TownList:
    """Represents a list of towns."""

    towns: list[Town]

    def __iter__(self):
        yield from self.towns

    def get_by_name(self, name: str | TownName) -> Town:
        """Get town by name."""
        if isinstance(name, TownName):
            name: str = name.name

        # There should only be one element here.
        return next(town for town in self.towns if town.name.name == name)


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

    def get_by_name(self, name: str | CountryName) -> Country:
        """Get town by name."""
        if isinstance(name, CountryName):
            name: str = name.name
        # There should only be one element here.
        return next(country for country in self.countries if country.name.name == name)
