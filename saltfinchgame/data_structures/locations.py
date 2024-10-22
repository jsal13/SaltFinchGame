from enum import Enum, auto

from attrs import define


class Size(Enum):
    """Size of the Area."""

    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()


class Biome(Enum):
    """Biomes of Areas."""

    FOREST = auto()
    TUNDRA = auto()
    DESERT = auto()
    GRASSLAND = auto()


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

    name: str
    description: Description


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
