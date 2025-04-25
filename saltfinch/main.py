import time
from attrs import define

from saltfinch.game.game import Game
from saltfinch.common.terminal import Terminal

# from saltfinch._data.game.game import start_script


@define
class GameLoop:
    """
    Main game loop that handles user input and game state.
    """

    game: Game = Game()

    def run(self):
        # start_script(delay=0.01)
        input("Press Enter to start the game...")

        Terminal.print_header(day=self.game.day, money=self.game.player.money)
        self.game.current_town_economy.display_goods(
            player_inventory=self.game.player.inventory
        )

        while True:
            command = Terminal.get_command()

            if command == "quit":
                print("Thanks for playing!")
                break

            elif command == "next":
                Terminal.print_header(day=self.game.day, money=self.game.player.money)
                self.game.advance_day()
                self.game.current_town_economy.display_events()
                self.game.current_town_economy.display_goods(
                    player_inventory=self.game.player.inventory
                )

            elif command == "inventory":
                Terminal.print_header(self.game.day, self.game.player.money)
                self.game.player.display_inventory(
                    current_town_economy=self.game.current_town_economy
                )
                self.game.current_town_economy.display_goods(
                    player_inventory=self.game.player.inventory
                )

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
                elif action == "sell":
                    success, message = self.game.sell(good_name, quantity)
                else:
                    print("Invalid action. Use 'buy' or 'sell'.")
                    continue

                print(message)
                time.sleep(1)  # Brief pause to read the message

                Terminal.print_header(self.game.day, self.game.player.money)
                self.game.current_town_economy.display_goods(
                    player_inventory=self.game.player.inventory
                )

            else:
                print("Unknown command. Try again.")


if __name__ == "__main__":
    game = GameLoop()
    game.run()
