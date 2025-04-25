"""
Functions for terminal operations.
"""

import os
import time

from attrs import define


@define
class Terminal:
    """
    A class to handle terminal operations.
    """

    @staticmethod
    def clear_screen() -> None:
        """Clears the terminal screen."""
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def slow_print(text: str | list[str], delay: float = 0.03) -> None:
        """
        Prints text to the terminal with a delay between each character.
        """
        if isinstance(text, list):
            text = "\n".join(text)

        for char in text:
            print(char, end="", flush=True)
            time.sleep(delay)

    @staticmethod
    def print_divider(
        character: str = "=",
        space_before: bool = False,
        space_after: bool = True,
        length: int = 60,
    ) -> None:
        """Prints a divider line in the terminal."""
        newline = "\n"
        character = (
            f"{newline if space_before else ''}"
            + f"{character * length}"
            + f"{newline if space_after else ''}"
        )

        print(character)

    @staticmethod
    def print_header(day: int, money: float) -> None:
        """
        Prints the game header with the current day and money.
        """
        Terminal.clear_screen()
        print(f"=== SALTFINCH - Day {day} ===")
        print(f"Money: ${money}")
        Terminal.print_divider()

    @staticmethod
    def get_command() -> str:
        """
        Prompts the user for a command and returns it.
        """
        print("Commands:")
        print("- buy <good> <quantity>: Buy goods")
        print("- sell <good> <quantity>: Sell goods")
        print("- next: Move to the next day")
        print("- inventory: Display your inventory")
        print("- quit: Exit the game")
        Terminal.print_divider()

        return input("What would you like to do? ").strip().lower()
