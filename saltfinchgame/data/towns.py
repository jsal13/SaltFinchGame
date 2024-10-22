from enum import Enum, auto

from saltfinchgame.data_structures.locations import Town


class TownName(Enum):
    """Town name enum."""

    AETHERBURG = auto()
    BOREALIS = auto()
    CAERWYN = auto()
    CALIDUS = auto()
    DUNARD = auto()
    DURUM = auto()
    ELLAN = auto()
    EOS = auto()
    FRIGIDUM = auto()
    GAELIC = auto()
    GLACIALIS = auto()
    GOROD = auto()
    IGNIS = auto()
    KIL = auto()
    KRASNOYE = auto()
    LUNA = auto()
    NOVOSIBIRSK = auto()
    NOX = auto()
    STARY = auto()
    ZOLOTOY = auto()


TOWNS = {
    TownName.CAERWYN: Town(name="Caerwyn", goods_selling="", goods_buying=""),
    TownName.AETHERBURG: Town(name="Aetherburg", goods_selling="", goods_buying=""),
    TownName.BOREALIS: Town(name="Borealis", goods_selling="", goods_buying=""),
    TownName.CALIDUS: Town(name="Calidus", goods_selling="", goods_buying=""),
    TownName.DURUM: Town(name="Durum", goods_selling="", goods_buying=""),
    TownName.EOS: Town(name="Eos", goods_selling="", goods_buying=""),
    TownName.FRIGIDUM: Town(name="Frigidum", goods_selling="", goods_buying=""),
    TownName.IGNIS: Town(name="Ignis", goods_selling="", goods_buying=""),
    TownName.LUNA: Town(name="Luna", goods_selling="", goods_buying=""),
    TownName.NOX: Town(name="Nox", goods_selling="", goods_buying=""),
    TownName.DUNARD: Town(name="Dunard", goods_selling="", goods_buying=""),
    TownName.ELLAN: Town(name="Ellan", goods_selling="", goods_buying=""),
    TownName.GAELIC: Town(name="Gaelic", goods_selling="", goods_buying=""),
    TownName.KIL: Town(name="Kil", goods_selling="", goods_buying=""),
    TownName.GOROD: Town(name="Gorod", goods_selling="", goods_buying=""),
    TownName.KRASNOYE: Town(name="Krasnoye", goods_selling="", goods_buying=""),
    TownName.NOVOSIBIRSK: Town(name="Novosibirsk", goods_selling="", goods_buying=""),
    TownName.STARY: Town(name="Stary", goods_selling="", goods_buying=""),
    TownName.ZOLOTOY: Town(name="Zoloty", goods_selling="", goods_buying=""),
}
