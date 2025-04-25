import random
import sys
from typing import List, Dict


class Player:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.food = 100
        self.money = 250
        self.distance_traveled = 0
        self.days_passed = 0
        self.alive = True
        self.party_members = []  # Could be extended with companion characters
        self.inventory = {"medicine": 2, "spare parts": 3, "ammunition": 20}

    def __str__(self) -> str:
        return f"{self.name} - Health: {self.health}%, Food: {self.food} lbs, Money: ${self.money}"


class Town:
    def __init__(self, name: str, distance: int, prices: Dict[str, int]):
        self.name = name
        self.distance = distance  # Distance from starting point
        self.prices = prices  # Different prices for each town

    def __str__(self) -> str:
        return f"{self.name} - {self.distance} miles from start"



class Game:
    def __init__(self):
        self.player = None
        self.current_town_index = 0
        self.towns = self._initialize_towns()
        self.events = self._initialize_events()

    def _initialize_towns(self) -> List[Town]:
        return [
            Town(
                "Independence",
                0,
                {"food": 1, "medicine": 15, "spare parts": 10, "ammunition": 1},
            ),
            Town(
                "Fort Kearney",
                250,
                {"food": 2, "medicine": 20, "spare parts": 15, "ammunition": 2},
            ),
            Town(
                "Fort Laramie",
                500,
                {"food": 3, "medicine": 25, "spare parts": 20, "ammunition": 2},
            ),
            Town(
                "Fort Bridger",
                750,
                {"food": 3, "medicine": 30, "spare parts": 25, "ammunition": 3},
            ),
            Town(
                "Fort Hall",
                1000,
                {"food": 4, "medicine": 35, "spare parts": 30, "ammunition": 3},
            ),
            Town(
                "Fort Boise",
                1200,
                {"food": 4, "medicine": 40, "spare parts": 35, "ammunition": 4},
            ),
            Town(
                "Fort Walla Walla",
                1400,
                {"food": 5, "medicine": 45, "spare parts": 40, "ammunition": 4},
            ),
            Town(
                "Oregon City",
                1600,
                {"food": 5, "medicine": 50, "spare parts": 45, "ammunition": 5},
            ),
        ]

    def show_status(self):
        self.clear_screen()
        print(f"\n{'=' * 60}")
        print(f"CURRENT STATUS - Day {self.player.days_passed}")
        print(f"{'=' * 60}")
        print(f"{self.player}")
        print(f"Distance traveled: {self.player.distance_traveled} miles")
        print(f"Current location: {self.towns[self.current_town_index].name}")

        # Show inventory
        print("\nInventory:")
        for item, amount in self.player.inventory.items():
            print(f"- {item.capitalize()}: {amount}")

        print(f"{'=' * 60}\n")

    def handle_town_options(self):
        town = self.towns[self.current_town_index]

        while True:
            self.show_status()
            print(f"Welcome to {town.name}!")
            print("\nWhat would you like to do?")
            print("1. Buy supplies")
            print("2. Rest and heal")
            print("3. Continue your journey")

            choice = input("\nEnter your choice (1-3): ")

            if choice == "1":
                self.buy_supplies(town)
            elif choice == "2":
                self.rest_and_heal()
            elif choice == "3":
                if self.current_town_index == len(self.towns) - 1:
                    self.game_won()
                    return
                return  # Exit town and continue journey
            else:
                print("Invalid choice. Please try again.")

    def buy_supplies(self, town: Town):
        while True:
            self.show_status()
            print(f"Store Prices in {town.name}:")
            print(f"{'=' * 60}")

            items = list(town.prices.keys())
            for i, item in enumerate(items, 1):
                print(f"{i}. {item.capitalize()}: ${town.prices[item]} each")

            print(f"{len(items) + 1}. Return to town options")

            try:
                choice = int(input("\nEnter your choice: "))
                if choice == len(items) + 1:
                    return

                if 1 <= choice <= len(items):
                    item = items[choice - 1]
                    max_affordable = self.player.money // town.prices[item]

                    if max_affordable == 0:
                        print("You can't afford any of this item.")
                        input("Press Enter to continue...")
                        continue

                    print(f"You can afford up to {max_affordable} {item}.")
                    amount = int(input(f"How many {item} would you like to buy? "))

                    if amount <= 0:
                        print("Purchase cancelled.")
                    elif amount > max_affordable:
                        print("You can't afford that many.")
                    else:
                        cost = amount * town.prices[item]
                        self.player.money -= cost

                        if item == "food":
                            self.player.food += amount
                        else:
                            self.player.inventory[item] = (
                                self.player.inventory.get(item, 0) + amount
                            )

                        print(f"You purchased {amount} {item} for ${cost}.")

                    input("Press Enter to continue...")
                else:
                    print("Invalid choice. Please try again.")
                    input("Press Enter to continue...")
            except ValueError:
                print("Please enter a number.")
                input("Press Enter to continue...")

    def rest_and_heal(self):
        self.show_status()
        print("You decide to rest for a few days.")

        days = int(input("How many days would you like to rest? (1-5): "))
        days = max(1, min(5, days))  # Ensure between 1-5 days

        # Each day of rest
        for _ in range(days):
            # Recover health
            self.player.health = min(100, self.player.health + 5)

            # Consume food
            food_consumed = 2  # Food consumed per day
            self.player.food = max(0, self.player.food - food_consumed)

            # Check if ran out of food
            if self.player.food <= 0:
                self.player.health = max(
                    0, self.player.health - 10
                )  # Lose health if no food
                if self.player.health <= 0:
                    self.player.alive = False
                    print("You have died of starvation.")
                    input("Press Enter to continue...")
                    return

            # Increment days
            self.player.days_passed += 1

        print(f"After {days} days of rest, your health is now {self.player.health}%.")
        input("Press Enter to continue...")

    def travel_to_next_town(self):
        if self.current_town_index >= len(self.towns) - 1:
            return

        current_town = self.towns[self.current_town_index]
        next_town = self.towns[self.current_town_index + 1]

        distance = next_town.distance - current_town.distance
        days_needed = distance // 20  # Travel 20 miles per day

        print(f"\nYou're heading to {next_town.name}, {distance} miles away.")
        print(f"The journey will take approximately {days_needed} days.")
        input("Press Enter to begin your journey...")

        # Daily travel loop
        for day in range(1, days_needed + 1):
            if not self.player.alive:
                return

            self.show_status()
            print(
                f"Day {self.player.days_passed + 1} of your journey to {next_town.name}"
            )
            print(
                f"You've traveled {(day - 1) * 20} miles of the {distance} mile journey."
            )

            # Consume food daily
            daily_food = 2  # Food consumed per day per person
            self.player.food = max(0, self.player.food - daily_food)

            # Check if ran out of food
            if self.player.food <= 0:
                self.player.health = max(
                    0, self.player.health - 10
                )  # Lose health if no food
                print("You've run out of food and are losing health!")

                if self.player.health <= 0:
                    self.player.alive = False
                    print("You have died of starvation.")
                    input("Press Enter to continue...")
                    return

            # Random events (70% chance per day)
            if random.random() < 0.7 and self.events:
                self.handle_random_event()

            # Check if player is still alive
            if not self.player.alive:
                return

            # Update days and distance
            self.player.days_passed += 1
            self.player.distance_traveled = current_town.distance + (day * 20)

            # If this is not the last day, pause for player input
            if day < days_needed:
                input("\nPress Enter to continue to the next day...")

        # Arrived at next town
        self.current_town_index += 1
        self.player.distance_traveled = next_town.distance
        print(f"\nYou've arrived at {next_town.name}!")
        input("Press Enter to continue...")

    def handle_random_event(self):
        # Select a random event
        event = random.choice(self.events)

        self.clear_screen()
        print(f"\n{'!' * 60}")
        print(f"EVENT: {event.name}")
        print(f"{'!' * 60}")
        self.slow_print(event.description)
        print("\nWhat will you do?")

        # Show choices
        for i, choice in enumerate(event.choices, 1):
            print(f"{i}. {choice}")

        # Get player choice
        while True:
            try:
                choice = int(input("\nEnter your choice: "))
                if 1 <= choice <= len(event.choices):
                    # Modified to handle inventory items
                    if event.name == "Illness" and choice == 1:
                        if self.player.inventory.get("medicine", 0) > 0:
                            self.player.inventory["medicine"] -= 1
                        else:
                            print("You don't have any medicine!")
                            continue
                    elif event.name == "Broken Wagon" and choice == 1:
                        if self.player.inventory.get("spare parts", 0) > 0:
                            self.player.inventory["spare parts"] -= 1
                        else:
                            print("You don't have any spare parts!")
                            continue
                    elif event.name == "Bandits" and choice == 1:
                        if self.player.inventory.get("ammunition", 0) >= 5:
                            self.player.inventory["ammunition"] -= 5
                        else:
                            print("You don't have enough ammunition to fight!")
                            continue

                    # Process the outcome
                    result = event.occur(self.player, choice - 1)
                    self.slow_print(f"\n{result}")
                    input("\nPress Enter to continue...")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")

    def game_over(self):
        self.clear_screen()
        print("\n" + "=" * 60)
        print("GAME OVER")
        print("=" * 60)
        print(
            f"\nYou died after traveling {self.player.distance_traveled} miles in {self.player.days_passed} days."
        )
        print("\nBetter luck next time on the trail!")
        print("\nThank you for playing!")
        input("\nPress Enter to exit...")
        sys.exit()

    def game_won(self):
        self.clear_screen()
        print("\n" + "=" * 60)
        print("CONGRATULATIONS!")
        print("=" * 60)
        print(
            f"\nYou've reached Oregon City after {self.player.days_passed} days on the trail!"
        )
        print(f"Final Statistics:")
        print(f"- Health: {self.player.health}%")
        print(f"- Food Remaining: {self.player.food} lbs")
        print(f"- Money Remaining: ${self.player.money}")
        print("\nYou've successfully completed your journey!")
        print("\nThank you for playing!")
        input("\nPress Enter to exit...")
        sys.exit()

        while self.player.alive:
            self.handle_town_options()

            if not self.player.alive:
                self.game_over()
                break

            if self.current_town_index < len(self.towns) - 1:
                self.travel_to_next_town()
            else:
                break  # Game finished

        if not self.player.alive:
            self.game_over()


if __name__ == "__main__":
    game = Game()
    game.start()
