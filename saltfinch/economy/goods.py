"""
Class representing a good in the economy.
This class is used to create goods that can be bought and sold in the economy."""
from attrs import define, field


@define
class Good:
    """
    Represents a good that can be bought and sold in the economy.
    Each good has a name, a base price, and a volatility factor that determines
    how much the price can fluctuate day to day.
    """

    name: str
    base_price: int = field(default=1)
     # How much the price can fluctuate day to day
    volatility: float = field(default=1)
    current_price: int = field(default=1, init=False)

    @classmethod
    def create(cls, name: str, base_price: int, volatility: float) -> "Good":
        good_class: "Good" = cls(
            name=name, base_price=base_price, volatility=volatility
        )
        good_class.current_price = good_class.base_price
        return good_class
