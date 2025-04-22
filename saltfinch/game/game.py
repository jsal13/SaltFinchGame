from attrs import define, field

from saltfinch.economy.town_economies import TownEconomy
from saltfinch.game.player import Player
from saltfinch.data.economy.town_economies import TOWN_ECONOMIES

@define
class Game:
    day: int = field(default=1)
    current_town_economy: "TownEconomy" = field(default=TOWN_ECONOMIES["forest"])
    player: "Player" = field(factory=lambda: Player(money=1000, inventory={}))

    def advance_day(self):
        self.day += 1
        # TODO: This also updates events:
        self.current_town_economy.update_prices()

    def buy(self, good_name: str, quantity: int) -> tuple[bool, str]:
        if good_name not in self.current_town_economy.goods:
            return False, f"Good '{good_name}' does not exist."

        total_cost = self.current_town_economy.goods[good_name].current_price * quantity

        if total_cost > self.player.money:
            return False, "Not enough money for this purchase."

        self.player.money -= total_cost
        self.player.inventory[good_name] = (
            self.player.inventory.get(good_name, 0) + quantity
        )

        return (
            True,
            f"Bought {quantity} {self.current_town_economy.goods[good_name].name} for ${total_cost:.2f}.",
        )

    def sell(self, good_name: str, quantity: int) -> tuple[bool, str]:
        if good_name not in self.current_town_economy.goods:
            return False, f"Good '{good_name}' does not exist."

        if (
            good_name not in self.player.inventory
            or self.player.inventory[good_name] < quantity
        ):
            return False, "Not enough of this item in your inventory."

        total_price = (
            self.current_town_economy.goods[good_name].current_price * quantity
        )
        self.player.money += total_price
        self.player.inventory[good_name] -= quantity

        if self.player.inventory[good_name] == 0:
            del self.player.inventory[good_name]

        return (
            True,
            f"Sold {quantity} {self.current_town_economy.goods[good_name].name} for ${total_price:.2f}.",
        )
