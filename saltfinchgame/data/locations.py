from saltfinchgame.data.items import (
    TOWN_AETHERBURG_ITEM_POOL,
    TOWN_BOREALIS_ITEM_POOL,
    TOWN_CAERWYN_ITEM_POOL,
)
from saltfinchgame.data_structures.ascii_map import MapLocation
from saltfinchgame.data_structures.locations import (
    Country,
    CountryList,
    Description,
    Town,
    TownList,
)

list_of_towns: list[Town] = [
    # FALIAS
    Town(
        name="CAERWYN",
        description="",
        country="FALIAS",
        map_location=MapLocation(3, 5),
        item_list=TOWN_CAERWYN_ITEM_POOL,
        inn_cost=1,
    ),
    Town(
        name="AETHERBURG",
        description="",
        country="FALIAS",
        map_location=MapLocation(40, 3),
        item_list=TOWN_AETHERBURG_ITEM_POOL,
        inn_cost=1,
    ),
    Town(
        name="BOREALIS",
        description="",
        country="FALIAS",
        map_location=MapLocation(8, 9),
        item_list=TOWN_BOREALIS_ITEM_POOL,
        inn_cost=1,
    ),
    # SCHOLOMANCE
    Town(
        name="CALIDUS",
        description="",
        country="SCHOLOMANCE",
        map_location=MapLocation(),
        item_list=None,
        inn_cost=1,
    ),
    Town(
        name="DUNARD",
        description="",
        country="SCHOLOMANCE",
        map_location=MapLocation(),
        item_list=None,
        inn_cost=1,
    ),
    Town(
        name="DURUM",
        description="",
        country="SCHOLOMANCE",
        map_location=MapLocation(),
        item_list=None,
        inn_cost=1,
    ),
    Town(
        name="ELLAN",
        description="",
        country="SCHOLOMANCE",
        map_location=MapLocation(),
        item_list=None,
        inn_cost=1,
    ),
    Town(
        name="EOS",
        description="",
        country="SCHOLOMANCE",
        map_location=MapLocation(),
        item_list=None,
        inn_cost=1,
    ),
    # ZERZURA
    Town(
        name="FRIGIDUM",
        description="",
        country="ZERZURA",
        map_location=MapLocation(),
        item_list=None,
        inn_cost=1,
    ),
    Town(
        name="GAELIC",
        description="",
        country="ZERZURA",
        map_location=MapLocation(),
        item_list=None,
        inn_cost=1,
    ),
    Town(
        name="GLACIALIS",
        description="",
        country="ZERZURA",
        map_location=MapLocation(),
        item_list=None,
        inn_cost=1,
    ),
    # KARSHVAR
    Town(
        name="LUNA",
        description="",
        country="KARSHVAR",
        map_location=MapLocation(),
        item_list=None,
        inn_cost=1,
    ),
    # Town(
    #     name="IGNIS",
    #     description="",
    #     country="
    # "     map_location=MapLocation(),
    #     items_selling="",
    #     items_buying="",
    #       inn_cost=1
    # ),
    # Town(
    #     name="NOX",
    #     description="",
    #     country="
    # "     map_location=MapLocation(),
    #     items_selling="",
    #     items_buying="",
    #       inn_cost=1
    # ),
    # Town(
    #     name="KIL",
    #     description="",
    #     country="
    # "     map_location=MapLocation(),
    #     items_selling="",
    #     items_buying="",
    #       inn_cost=1
    # ),
    # Town(
    #     name="GOROD",
    #     description="",
    #     country="
    # "     map_location=MapLocation(),
    #     items_selling="",
    #     items_buying="",
    #       inn_cost=1
    # ),
    # Town(
    #     name="KRASNOYE",
    #     description="",
    #     country="
    # "     map_location=MapLocation(),
    #     items_selling="",
    #     items_buying="",
    #       inn_cost=1
    # ),
    # Town(
    #     name="NOVOSIBIRSK",
    #     description="",
    #     country="
    # "     map_location=MapLocation(),
    #     items_selling="",
    #     items_buying="",
    #       inn_cost=1
    # ),
    # Town(
    #     name="STARY",
    #     description="",
    #     country="
    # "     map_location=MapLocation(),
    #     items_selling="",
    #     items_buying="",
    #       inn_cost=1
    # ),
    # Town(
    #     name="ZOLOTOY",
    #     description="",
    #     country="
    # "     map_location=MapLocation(),
    #     items_selling="",
    #     items_buying="",
    #       inn_cost=1
    # ),
]

TOWNS: TownList = TownList(towns=list_of_towns)

# TOWNS must be defined before Countries is able to grab from them.
list_of_countries: list[Country] = [
    Country(
        name="FALIAS",
        towns=TownList(
            towns=[
                TOWNS.get_by_name("AETHERBURG"),
                TOWNS.get_by_name("BOREALIS"),
                TOWNS.get_by_name("CAERWYN"),
            ]
        ),
        map_location=MapLocation(x=3, y=1),
        description=Description(
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
        name="SCHOLOMANCE",
        towns=TownList(
            towns=[
                TOWNS.get_by_name("CALIDUS"),
                TOWNS.get_by_name("DUNARD"),
                TOWNS.get_by_name("DURUM"),
                TOWNS.get_by_name("ELLAN"),
                TOWNS.get_by_name("EOS"),
            ]
        ),
        map_location=MapLocation(x=5, y=7),
        description=Description(
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
        name="ZERZURA",
        towns=TownList(
            towns=[
                TOWNS.get_by_name("FRIGIDUM"),
                TOWNS.get_by_name("GAELIC"),
                TOWNS.get_by_name("GLACIALIS"),
            ]
        ),
        map_location=MapLocation(x=22, y=12),
        description=Description(
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
    #     name="AKHET",
    #     towns=TownList(towns=[
    #         TOWNS.get_by_name("GOROD"),
    #         TOWNS.get_by_name("IGNIS"),
    #     ]),
    #     description=Description(
    #         weather="Warm winters with humid, hot summers.",
    #         resources=(
    #             "Cotton and rice grow well here.  Some textiles and pottery can be "
    #             "found in the cities."
    #         ),
    #         misc_facts="",
    #     ),
    # ),
    Country(
        name="KARSHVAR",
        towns=TownList(
            towns=[
                TOWNS.get_by_name("LUNA"),
            ]
        ),
        map_location=MapLocation(x=37, y=3),
        description=Description(
            weather="Warm winters with humid, hot summers.",
            resources="",
            misc_facts="",
        ),
    ),
]

COUNTRIES: CountryList = CountryList(countries=list_of_countries)
