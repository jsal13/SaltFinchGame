from enum import Enum, auto

from saltfinchgame.data.towns import TOWNS, TownName
from saltfinchgame.data_structures.locations import Biome, Country, Description, Size


class CountryName(Enum):
    """Enum for country name."""

    FALIAS = auto()
    SCHOLOMANCE = auto()
    ZERZURA = auto()
    AKHET = auto()
    KARSHVAR = auto()


COUNTRIES: dict[CountryName, "Country"] = {
    CountryName.FALIAS: Country(
        name="Falias",
        num_towns=3,
        towns=[
            TOWNS[TownName.AETHERBURG],
            TOWNS[TownName.BOREALIS],
            TOWNS[TownName.CAERWYN],
        ],
        description=Description(
            size=Size.SMALL,
            biomes=[Biome.FOREST, Biome.GRASSLAND],
            weather="Temperate weather, neither too hot nor too cold.",
            resources=(
                "The soil is typically loamy, with a good balance of sand, silt, "
                "and clay. This type of soil is well-suited for agriculture, "
                "particularly for growing crops like wheat and sugar beets."
            ),
            misc_facts=(
                "The Tuatha Dé Danann acquired one of their four treasures here."
            ),
        ),
    ),
    CountryName.Scholomance: Country(
        name="Scholomance",
        num_towns=5,
        towns=[
            TOWNS[TownName.CALIDUS],
            TOWNS[TownName.DUNARD],
            TOWNS[TownName.DURUM],
            TOWNS[TownName.ELLAN],
            TOWNS[TownName.EOS],
        ],
        description=Description(
            size=Size.LARGE,
            biomes=[Biome.FOREST, Biome.TUNDRA],
            weather="Continental climate: hot, dry summers and cold, snowy winters.",
            resources=(
                "The soil is typically sandy and loamy, allowing some "
                "agriculture to thrive.  Copper and lead can be found in the "
                "mountainous regions."
            ),
            misc_facts="",
        ),
    ),
    CountryName.ZERZURA: Country(
        name="Zerzura",
        num_towns=3,
        towns=[
            TOWNS[TownName.FRIGIDUM],
            TOWNS[TownName.GAELIC],
            TOWNS[TownName.GLACIALIS],
        ],
        description=Description(
            size=Size.MEDIUM,
            biomes=[Biome.DESERT],
            weather=(
                "Warm weather in the grassland portion in the north-west, the "
                "desert is extremely hot during the day and extremely cold during "
                "the night regardless of season."
            ),
            resources=(
                "Dates and pistachios can grow well here. Carpets and fine thread "
                "are made in the major cities."
            ),
            misc_facts="Sometimes called the 'oasis of little birds'.",
        ),
    ),
    CountryName.AKHET: Country(
        name="Akhet",
        num_towns=2,
        towns=[
            TOWNS[TownName.GOROD],
            TOWNS[TownName.IGNIS],
        ],
        description=Description(
            size=Size.SMALL,
            biomes=[Biome.DESERT, Biome.FOREST],
            weather="Warm winters with humid, hot summers.",
            resources=(
                "Cotton and rice grow well here.  Some textiles and pottery can be "
                "found in the cities."
            ),
            misc_facts="",
        ),
    ),
    CountryName.KARSHVAR: Country(
        name="Karshvar",
        num_towns=3,
        towns=[
            TOWNS[TownName.KIL],
            TOWNS[TownName.KRASNOYE],
            TOWNS[TownName.LUNA],
        ],
        description=Description(
            size=Size.SMALL,
            biomes=[Biome.GRASSLAND, Biome.FOREST],
            weather="Warm winters with humid, hot summers.",
            resources="",
            misc_facts="",
        ),
    ),
}
