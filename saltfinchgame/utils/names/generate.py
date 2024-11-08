"""
Generate names for traders, etc.

Names collected from the following sources:
 - <https://www.s-gabriel.org/names/juliana/16thcvenice.html>
"""

import random

from saltfinchgame.constants import NAMES


def generate_name() -> tuple[str, str]:
    """Generate a random first name and gives masc/femme for name type."""
    masc_names = [(name, "masc") for name in NAMES["masc"]]
    femme_names = [(name, "femme") for name in NAMES["femme"]]
    names_pool = masc_names + femme_names
    return random.choice(names_pool)


if __name__ == "__main__":
    print(generate_name())
