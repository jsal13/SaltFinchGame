from typing import TYPE_CHECKING
from attrs import define

from saltfinch.common.terminal import Terminal

if TYPE_CHECKING:  # pragma: no cover
    from saltfinch.economy.town_economies import TownEconomy


@define
class Player:
    health: int = 100
    water: int = 20
    money: int = 1000
    inventory: dict[str, int] = {}
    alive: bool = True
    is_in_town: bool = True
    is_traveling: bool = False

    def __str__(self) -> str:
        return (
            f"Player(health={self.health}, water={self.water}, "
            f"money={self.money}, inventory={self.inventory}, "
            f"alive={self.alive}, is_in_town={self.is_in_town}, "
            f"is_traveling={self.is_traveling})"
        )

    def display_inventory(self, current_town_economy: "TownEconomy") -> None:
        """
        Displays the player's inventory and its total value.
        """
        if not self.inventory:
            print("Your inventory is empty.")
            Terminal.print_divider()
            return

        print("Your Inventory:")
        total_value: int = 0
        for name, quantity in sorted(self.inventory.items()):
            good = current_town_economy.goods[name]
            value = quantity * good.current_price
            total_value += value
            print(f"{good.name}: {quantity} (worth ${value})")
        print(f"Total inventory value: ${total_value}")
        Terminal.print_divider()
