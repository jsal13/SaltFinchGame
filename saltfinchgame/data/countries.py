from saltfinchgame.data.location_names import CountryName, TownName
from saltfinchgame.data.towns import TOWNS
from saltfinchgame.data_structures.locations import (
    Biome,
    Country,
    CountryList,
    Description,
    MapLocation,
    Size,
)

list_of_countries: list[Country] = [
    Country(
        name=CountryName.FALIAS,
        towns=[
            TOWNS.get_by_name(TownName.AETHERBURG),
            TOWNS.get_by_name(TownName.BOREALIS),
            TOWNS.get_by_name(TownName.CAERWYN),
        ],
        map_location=MapLocation(x=3, y=1),
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
    Country(
        name=CountryName.SCHOLOMANCE,
        towns=[
            TOWNS.get_by_name(TownName.CALIDUS),
            TOWNS.get_by_name(TownName.DUNARD),
            TOWNS.get_by_name(TownName.DURUM),
            TOWNS.get_by_name(TownName.ELLAN),
            TOWNS.get_by_name(TownName.EOS),
        ],
        map_location=MapLocation(x=5, y=7),
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
    Country(
        name=CountryName.ZERZURA,
        towns=[
            TOWNS.get_by_name(TownName.FRIGIDUM),
            TOWNS.get_by_name(TownName.GAELIC),
            TOWNS.get_by_name(TownName.GLACIALIS),
        ],
        map_location=MapLocation(x=22, y=12),
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
    # Country(
    #     name=CountryName.AKHET,
    #     towns=[
    #         TOWNS.get_by_name(TownName.GOROD),
    #         TOWNS.get_by_name(TownName.IGNIS),
    #     ],
    #     description=Description(
    #         size=Size.SMALL,
    #         biomes=[Biome.DESERT, Biome.FOREST],
    #         weather="Warm winters with humid, hot summers.",
    #         resources=(
    #             "Cotton and rice grow well here.  Some textiles and pottery can be "
    #             "found in the cities."
    #         ),
    #         misc_facts="",
    #     ),
    # ),
    Country(
        name=CountryName.KARSHVAR,
        towns=[
            TOWNS.get_by_name(TownName.LUNA),
        ],
        map_location=MapLocation(x=37, y=3),
        description=Description(
            size=Size.SMALL,
            biomes=[Biome.GRASSLAND, Biome.FOREST],
            weather="Warm winters with humid, hot summers.",
            resources="",
            misc_facts="",
        ),
    ),
]

COUNTRIES: CountryList = CountryList(countries=list_of_countries)
