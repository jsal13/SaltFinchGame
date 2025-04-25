"""
Creates TownEconomy objects that represent the economy of a town.
These objects manage the goods available in the town and the economic events that can affect them.
"""

import random
import math
from copy import copy

from attrs import define, field

from saltfinch.economy.economic_events import EconomicEvent
from saltfinch.economy.goods import Good
from saltfinch.common.terminal import Terminal


@define
class TownEconomy:
    goods: dict[str, "Good"]
    economic_events: list["EconomicEvent"] = field(factory=list)
    daily_economic_events: list["EconomicEvent"] = field(init=False)

    def update_prices(self) -> None:
        # Clear previous day's events
        self.daily_economic_events = []

        # Placeholder for the current price of a good
        # This is a float because it can be affected by events.
        # It will be cast to an int at the end after rounding.
        current_price_raw: float

        # 30% chance of a random event occurring
        if random.random() < 0.3:
            event: "EconomicEvent" = random.choice(self.economic_events)
            affected_goods_in_common_with_goods: set[str] = set(
                event.affected_goods.keys()
            ).intersection(set(self.goods.keys()))

            # Only keep the affected goods that are in the town's goods.
            event.affected_goods = {
                good_name: event.affected_goods[good_name]
                for good_name in affected_goods_in_common_with_goods
            }

            if affected_goods_in_common_with_goods:
                # If some goods are affected, apply the event.
                self.daily_economic_events.append(event)

                # Apply event effects to goods prices
                for good_name, multiplier in event.affected_goods.items():
                    if good_name in self.goods:
                        current_price_raw = copy(self.goods[good_name].current_price)
                        current_price_raw *= multiplier

                    # Cast to integer.
                    self.goods[good_name].current_price = int(
                        round(current_price_raw, 0)
                    )

        # Natural price fluctuation for all goods
        for good in self.goods.values():
            # Random fluctuation based on volatility
            fluctuation = random.uniform(1 - good.volatility, 1 + good.volatility)
            current_price_raw = copy(good.current_price)
            current_price_raw *= fluctuation

            # Regression toward base price (market correction)
            correction_factor = 0.05  # 5% correction toward base price
            current_price_raw = (
                current_price_raw * (1 - correction_factor)
                + good.base_price * correction_factor
            )

            # Ensure price doesn't go too far from base price
            min_price = math.floor(good.base_price * 0.5)
            max_price = math.ceil(good.base_price * 3.5)
            current_price_raw = max(min_price, min(current_price_raw, max_price))

            # Cast to integer.
            good.current_price = int(round(current_price_raw, 0))

    def display_events(self):
        """Print the economic events that occurred today."""
        if self.daily_economic_events:
            print("Today's Events:")
            for event in self.daily_economic_events:
                print(f"{event.name}: {event.description}")
                print(f"Affected goods: {', '.join(event.affected_goods)}", end="\n")

    def display_goods(self, player_inventory: dict[str, int]) -> None:
        """Print the available goods in the town economy."""
        print("Available Goods:")
        print(f"{'Good': <10} {'Price': >8} {'Owned': >8} {'Value': >8} {'Change': >12}")
        Terminal.print_divider(character="-", space_before=False, space_after=False)

        # Creates a sorted list of goods based on their names, not enum values.
        for name, good in sorted(self.goods.items()):
            owned: int = player_inventory.get(name, 0)
            value: int = owned * good.current_price
            price_change: float = round(
                (good.current_price - good.base_price) / good.base_price * 100, 2
            )
            direction = "↑" if price_change > 0 else "↓" if price_change < 0 else "→"

            print(
                f"{good.name: <10} {good.current_price: >8} {owned: >8} {value: >8} {direction: >7} {abs(price_change):>3.1f}%"
            )
        Terminal.print_divider(space_before=True)
