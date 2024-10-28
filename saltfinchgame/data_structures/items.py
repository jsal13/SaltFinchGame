import math
from random import random

from attrs import define, field


@define()
class Item:
    """Parent class for items."""

    name: str
    buy_price: int | None = field(default=1)
    sell_price: int | None = field(default=None)
    probability_sold: float = field(default=1)

    def is_sold_today(self) -> bool:
        """Booleans given if the item will be sold today."""
        return self.probability_sold >= random()

    def get_buy_price(self) -> int:
        """Get the buy price of the item today."""
        if self.buy_price is None:
            return self.buy_price
        if self.sell_price is None:
            return self.buy_price

        _price = int(math.ceil(self.buy_price))
        if (_price <= 0) or (_price < self.sell_price):
            _price = self.sell_price + 1

        return _price

    def get_sell_price(self) -> int:
        """Get the sell price of the item today."""
        if self.buy_price is None:
            return self.sell_price
        if self.sell_price is None:
            return self.sell_price

        _price = int(math.ceil(self.sell_price))
        if (_price < 0) or (_price > self.sell_price):
            _price = 1

        return _price


@define()
class ItemList:
    """List of items."""

    items: list[Item]

    def __iter__(self):
        return iter(self.items)
