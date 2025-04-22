import random
from attrs import define, field

from saltfinch.economy.events import Event
from saltfinch.economy.goods import Good


@define
class TownEconomy:
    goods: dict[str, Good]
    events: list[Event] = field(factory=list)
    daily_events: list[Event] = field(init=False)

    def update_prices(self) -> None:
        # Clear previous day's events
        self.daily_events = []

        # 30% chance of a random event occurring
        if random.random() < 0.3:
            event = random.choice(self.events)
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
                self.daily_events.append(event)

                # Apply event effects to goods prices
                for good_name, multiplier in event.affected_goods.items():
                    if good_name in self.goods:
                        self.goods[good_name].current_price *= multiplier

        # Natural price fluctuation for all goods
        for good in self.goods.values():
            # Random fluctuation based on volatility
            fluctuation = random.uniform(1 - good.volatility, 1 + good.volatility)
            good.current_price *= fluctuation

            # Regression toward base price (market correction)
            correction_factor = 0.05  # 5% correction toward base price
            good.current_price = (
                good.current_price * (1 - correction_factor)
                + good.base_price * correction_factor
            )

            # Ensure price doesn't go too far from base price
            min_price = good.base_price * 0.5
            max_price = good.base_price * 2.0
            good.current_price = max(min_price, min(good.current_price, max_price))

            # Round to 2 decimal places for display
            good.current_price = round(good.current_price, 2)
