from saltfinchgame.data.location_names import CountryName, TownName
from saltfinchgame.data_structures.locations import MapLocation, Town, TownList

list_of_towns: list[Town] = [
    # FALIAS
    Town(
        name=TownName.CAERWYN,
        description="",
        country=CountryName.FALIAS,
        map_location=MapLocation(3, 5),
        goods_selling="",
        goods_buying="",
    ),
    Town(
        name=TownName.AETHERBURG,
        description="",
        country=CountryName.FALIAS,
        map_location=MapLocation(40, 3),
        goods_selling="",
        goods_buying="",
    ),
    Town(
        name=TownName.BOREALIS,
        description="",
        country=CountryName.FALIAS,
        map_location=MapLocation(8, 9),
        goods_selling="",
        goods_buying="",
    ),
    # SCHOLOMANCE
    Town(
        name=TownName.CALIDUS,
        description="",
        country=CountryName.SCHOLOMANCE,
        map_location=MapLocation(),
        goods_selling="",
        goods_buying="",
    ),
    Town(
        name=TownName.DUNARD,
        description="",
        country=CountryName.SCHOLOMANCE,
        map_location=MapLocation(),
        goods_selling="",
        goods_buying="",
    ),
    Town(
        name=TownName.DURUM,
        description="",
        country=CountryName.SCHOLOMANCE,
        map_location=MapLocation(),
        goods_selling="",
        goods_buying="",
    ),
    Town(
        name=TownName.ELLAN,
        description="",
        country=CountryName.SCHOLOMANCE,
        map_location=MapLocation(),
        goods_selling="",
        goods_buying="",
    ),
    Town(
        name=TownName.EOS,
        description="",
        country=CountryName.SCHOLOMANCE,
        map_location=MapLocation(),
        goods_selling="",
        goods_buying="",
    ),
    # ZERZURA
    Town(
        name=TownName.FRIGIDUM,
        description="",
        country=CountryName.ZERZURA,
        map_location=MapLocation(),
        goods_selling="",
        goods_buying="",
    ),
    Town(
        name=TownName.GAELIC,
        description="",
        country=CountryName.ZERZURA,
        map_location=MapLocation(),
        goods_selling="",
        goods_buying="",
    ),
    Town(
        name=TownName.GLACIALIS,
        description="",
        country=CountryName.ZERZURA,
        map_location=MapLocation(),
        goods_selling="",
        goods_buying="",
    ),
    # KARSHVAR
    Town(
        name=TownName.LUNA,
        description="",
        country=CountryName.KARSHVAR,
        map_location=MapLocation(),
        goods_selling="",
        goods_buying="",
    ),
    # Town(
    #     name=TownName.IGNIS,
    #     description="",
    #     country=CountryName.
    #     map_location=MapLocation(),
    #     goods_selling="",
    #     goods_buying="",
    # ),
    # Town(
    #     name=TownName.NOX,
    #     description="",
    #     country=CountryName.
    #     map_location=MapLocation(),
    #     goods_selling="",
    #     goods_buying="",
    # ),
    # Town(
    #     name=TownName.KIL,
    #     description="",
    #     country=CountryName.
    #     map_location=MapLocation(),
    #     goods_selling="",
    #     goods_buying="",
    # ),
    # Town(
    #     name=TownName.GOROD,
    #     description="",
    #     country=CountryName.
    #     map_location=MapLocation(),
    #     goods_selling="",
    #     goods_buying="",
    # ),
    # Town(
    #     name=TownName.KRASNOYE,
    #     description="",
    #     country=CountryName.
    #     map_location=MapLocation(),
    #     goods_selling="",
    #     goods_buying="",
    # ),
    # Town(
    #     name=TownName.NOVOSIBIRSK,
    #     description="",
    #     country=CountryName.
    #     map_location=MapLocation(),
    #     goods_selling="",
    #     goods_buying="",
    # ),
    # Town(
    #     name=TownName.STARY,
    #     description="",
    #     country=CountryName.
    #     map_location=MapLocation(),
    #     goods_selling="",
    #     goods_buying="",
    # ),
    # Town(
    #     name=TownName.ZOLOTOY,
    #     description="",
    #     country=CountryName.
    #     map_location=MapLocation(),
    #     goods_selling="",
    #     goods_buying="",
    # ),
]

TOWNS: TownList = TownList(towns=list_of_towns)
