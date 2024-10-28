from prompt_toolkit import HTML, print_formatted_text, prompt

from saltfinchgame.constants import ASCII_STYLES
from saltfinchgame.data.items import Item
from saltfinchgame.data.locations import TOWNS
from saltfinchgame.data_structures.locations import Town
from saltfinchgame.ui.clear_terminal import clear_terminal
from saltfinchgame.ui.input_validator import numeric_validator


def print_main_trade_screen(town: Town) -> None:
    """Display the main town screen."""
    title_01: HTML = HTML(
        f"{'=' * len(town.name)}\n"
        f"<town>{town.name}</town>"
        f"\n{'=' * len(town.name)}\n"
    )
    dialogue_01: HTML = HTML(
        f"You're standing in the <town>{town.name}</town> marketplace.\n"
        "They have the following items: \n"
    )

    print_formatted_text(title_01, style=ASCII_STYLES)
    print_formatted_text(dialogue_01, style=ASCII_STYLES)


def print_trade_items(town: Town) -> None:
    """Print trading item options."""
    item_mapping: dict[int, Item] = dict(enumerate(town.item_list))
    item_list_str: str = "".join(
        [
            f"{'': <4}{'ITEM': <14}| {'BUY': <5}| {'SELL': <5}|\n",
            # (" " * 4) + "ITEM" + (" " * 16) + "COST" + (" " * 6) + "SELL FOR" + "\n",
            ("-" * 18) + "+" + ("-" * 6) + "+" + ("-" * 6) + "+" + "-" "\n",
        ]
    )
    for n, item in item_mapping.items():
        buy_price: int = item.get_buy_price()
        sell_price: int = item.get_sell_price()

        str_buy_price: str = "" if buy_price is None else str(buy_price)
        str_sell_price: str = "" if sell_price is None else str(sell_price)

        item_list_str += (
            f"[{n}] {item.name: <14}| <buy>{str_buy_price: >4}</buy> | "
            f"<sell>{str_sell_price: >4}</sell> |\n"
        )

    options_html: HTML = HTML(item_list_str)
    print_formatted_text(options_html, style=ASCII_STYLES)


# def prompt_user_for_town_option_input() -> int:
#     """Prompt user for town option input."""
#     user_input: str

#     while True:
#         user_input = prompt("[Enter Number]> ", validator=numeric_validator).strip()
#         if int(user_input) in [1, 2, 3]:
#             break
#         else:
#             print(f"{user_input} is not in [1, 2, 3].")

#     return int(user_input)


# def handle_trade_in_marketplace(town: Town) -> None:
#     """Handle player choosing to trade in marketplace."""
#     pass


if __name__ == "__main__":
    caerwyn: Town = TOWNS.get_by_name("CAERWYN")
    clear_terminal()
    print_main_trade_screen(town=caerwyn)
    print()
    print_trade_items(town=caerwyn)
    # user_option_choice: int = prompt_user_for_town_option_input()
    # print(user_option_choice)
