"""
Creates misc gameplay functions for the game.
"""

from saltfinch.common.terminal import Terminal


def start_script(delay: float = 0.03) -> None:
    """
    Starts the game script with an introduction.
    """
    Terminal.clear_screen()
    print("\n" + "=" * 60)
    print("SALT FINCH")
    print("=" * 60)
    Terminal.slow_print(
        text=[
            "\nYou are a merchant trading goods in the desert state of Graff.",
            "You are trying to make enough money to travel to your family in",
            "the eastern city of Tazir.",
            "\nYou will have to make money by trading goods in the desert,",
            "but be careful: the desert is a dangerous place.",
            "\n\n",
        ],
        delay=delay,
    )
