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
class Country(Area):
    """Represents a Country."""

    num_towns: int
    towns: list["Town"]


@define()
class Town(Area):
    """Represents a Town/City."""

    goods_selling: str
    goods_buying: str
    country: "Country"
