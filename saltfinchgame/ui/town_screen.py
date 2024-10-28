from prompt_toolkit import HTML, print_formatted_text, prompt

from saltfinchgame.constants import ASCII_STYLES
from saltfinchgame.data.locations import TOWNS
from saltfinchgame.data_structures.locations import Town
from saltfinchgame.ui.clear_terminal import clear_terminal
from saltfinchgame.ui.input_validator import numeric_validator


def print_main_town_screen(town: Town) -> None:
    """Display the main town screen."""
    title_01: HTML = HTML(
        f"{'=' * len(town.name)}\n"
        f"<town>{town.name}</town>"
        f"\n{'=' * len(town.name)}\n"
    )
    dialogue_01: HTML = HTML(
        f"You're standing in the <town>{town.name}</town> town square.\n"
    )
    dialogue_02: HTML = HTML("What would you like to do?")

    print_formatted_text(title_01, style=ASCII_STYLES)
    print_formatted_text(dialogue_01, style=ASCII_STYLES)
    print_formatted_text(dialogue_02, style=ASCII_STYLES)


def print_town_options(town: Town) -> None:
    """Print options related to the town."""
    options: str = (
        f"""
    [1] Go to the inn and rest ({town.inn_cost} silver).
    [2] Trade in the marketplace.
    [3] Leave <town>{town.name}</town>.
    """
    )
    options_html: HTML = HTML(options)
    print_formatted_text(options_html, style=ASCII_STYLES)


def prompt_user_for_town_option_input() -> int:
    """Prompt user for town option input."""
    user_input: str

    while True:
        user_input = prompt("[Enter Number]> ", validator=numeric_validator).strip()
        if int(user_input) in [1, 2, 3]:
            break
        else:
            print(f"{user_input} is not in [1, 2, 3].")

    return int(user_input)


if __name__ == "__main__":
    aetherburg: Town = TOWNS.get_by_name("AETHERBURG")
    clear_terminal()
    print_main_town_screen(town=aetherburg)
    print()
    print_town_options(town=aetherburg)
    user_option_choice: int = prompt_user_for_town_option_input()
    print(user_option_choice)
