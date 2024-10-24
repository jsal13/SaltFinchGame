from enum import Enum, auto

from attrs import define, field


@define()
class MapLocation:
    """Location on the ASCII Map."""

    x: int = field(default=0)
    y: int = field(default=0)

    def __iter__(self):
        return iter((self.x, self.y))


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
