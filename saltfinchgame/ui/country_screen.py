from prompt_toolkit import HTML, print_formatted_text, prompt

from saltfinchgame.constants import ASCII_STYLES
from saltfinchgame.data.towns import TOWNS
from saltfinchgame.data_structures.locations import Town, TownName
from saltfinchgame.ui.clear_terminal import clear_terminal
from saltfinchgame.ui.input_validator import numeric_validator
from saltfinchgame.ui.print_maps import print_map_of_country


def print_main_country_screen(town: Town) -> None:
    """
    Display the main country screen.

    Note: We use `town` here because the Player will always
    be at a town, and that town will always be in a country.
    """
    title_01: HTML = HTML(
        f"{'=' * len(town.country.name)}\n"
        f"<town>{town.country.name}</town>"
        f"\n{'=' * len(town.country.name)}\n"
    )
    dialogue_01: HTML = HTML(
        f"You're at the enterance of <town>{town.name.name}</town> "
        f"in the country of <country>{town.country.name}</country>, "
        "getting ready to leave.\n"
    )
    dialogue_02: HTML = HTML("What would you like to do?")

    print_formatted_text(title_01, style=ASCII_STYLES)
    print_formatted_text(dialogue_01, style=ASCII_STYLES)
    print_map_of_country(country_name=town.country)
    print()
    print_formatted_text(dialogue_02, style=ASCII_STYLES)


def print_country_options(town: Town) -> None:
    """Print options related to the country."""
    options: str = (
        f"""
    [1] Go back into {town.name.name}.
    [2] Set out for another town.
    [3] Set out for another country.
    """
    )
    options_html: HTML = HTML(options)
    print_formatted_text(options_html, style=ASCII_STYLES)


def prompt_user_for_country_option_input() -> int:
    """Prompt user for country option input."""
    user_input: str

    while True:
        user_input = prompt("[Enter Number]> ", validator=numeric_validator).strip()
        if int(user_input) in [1, 2, 3]:
            break
        else:
            print(f"{user_input} is not in [1, 2, 3].")

    return int(user_input)


if __name__ == "__main__":
    aetherburg: Town = TOWNS.get_by_name(TownName.AETHERBURG)
    clear_terminal()
    print_main_country_screen(town=aetherburg)
    print()
    print_country_options(town=aetherburg)
    user_option_choice: int = prompt_user_for_country_option_input()
    print(user_option_choice)
