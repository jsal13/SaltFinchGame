from attrs import define


@define()
class Item:
    """Parent class for items."""

    name: str
    description: str
    default_buy_price: int
    default_sell_price: int


@define()
class ItemList:
    """List of items."""

    items: list[Item]
