import time
import os
from attrs import define

from saltfinch.game.game import Game
from saltfinch.economy.events import EconomicEventType


@define
class GameLoop:
    game: Game = Game()

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def print_divider(
        self, character: str = "=", space_before: bool = False, space_after: bool = True
    ):
        if space_before:
            print()

        print(character * 60)

        if space_after:
            print()

    def print_header(self):
        self.clear_screen()
        print(f"=== SALTFINCH - Day {self.game.day} ===")
        print(f"Money: ${self.game.player.money:.2f}")
        self.print_divider()

    def display_events(self):
        if self.game.current_town_economy.daily_economic_events:
            print("Today's Events:")
            for event in self.game.current_town_economy.daily_economic_events:
                event_type_symbol = (
                    "✓"
                    if event.event_type == EconomicEventType.POSITIVE
                    else "✗" if event.event_type == EconomicEventType.NEGATIVE else "○"
                )
                print(f"{event_type_symbol} {event.name}: {event.description}")
                print(f"Affected goods: {', '.join(event.affected_goods)}")
                print()

    def display_goods(self):
        print("Available Goods:")
        print(f"{'Good':<12} {'Price':<8} {'Owned':<8} {'Value':<8}")
        self.print_divider(character="-", space_before=False, space_after=False)
        for name, good in sorted(self.game.current_town_economy.goods.items()):
            owned = self.game.player.inventory.get(name, 0)
            value = owned * good.current_price
            price_change = (good.current_price - good.base_price) / good.base_price
            direction = "↑" if price_change > 0 else "↓" if price_change < 0 else "→"

            print(
                f"{good.name:<12} ${good.current_price:<7.2f} {owned:<8} ${value:<7.2f} {direction}"
            )
        self.print_divider(space_before=True)

    def display_inventory(self):
        if not self.game.player.inventory:
            print("Your inventory is empty.")
            self.print_divider()
            return

        print("Your Inventory:")
        total_value = 0
        for name, quantity in sorted(self.game.player.inventory.items()):
            good = self.game.current_town_economy.goods[name]
            value = quantity * good.current_price
            total_value += value
            print(f"{good.name}: {quantity} (worth ${value:.2f})")
        print(f"Total inventory value: ${total_value:.2f}")
        self.print_divider()

    def get_command(self):
        print("Commands:")
        print("- buy <good> <quantity>: Buy goods")
        print("- sell <good> <quantity>: Sell goods")
        print("- next: Move to the next day")
        print("- inventory: Display your inventory")
        print("- quit: Exit the game")
        self.print_divider()

        return input("What would you like to do? ").strip().lower()

    def run(self):
        self.print_header()
        self.display_goods()

        while True:
            command = self.get_command()

            if command == "quit":
                print("Thanks for playing!")
                break

            elif command == "next":
                self.print_header()
                self.game.advance_day()
                self.display_events()
                self.display_goods()

            elif command == "inventory":
                self.print_header()
                self.display_inventory()
                self.display_goods()

            elif command.startswith("buy ") or command.startswith("sell "):
                parts = command.split()
                if len(parts) != 3:
                    print("Invalid command format. Use: [buy/sell] [good] [quantity]")
                    continue

                action, good_name, quantity = parts

                try:
                    quantity = int(quantity)
                    if quantity <= 0:
                        print("Quantity must be positive.")
                        continue
                except ValueError:
                    print("Quantity must be a number.")
                    continue

                if action == "buy":
                    success, message = self.game.buy(good_name, quantity)
                else:  # sell
                    success, message = self.game.sell(good_name, quantity)

                print(message)
                time.sleep(1)  # Brief pause to read the message

                self.print_header()
                self.display_goods()

            else:
                print("Unknown command. Try again.")


if __name__ == "__main__":
    game = GameLoop()
    game.run()
