from saltfinchgame.constants import STARTING_VALUES

# from saltfinchgame.data_structures.items import Items
from saltfinchgame.data_structures.player import Player

player = Player(
    name=STARTING_VALUES["Name"],
    health=STARTING_VALUES["Health"],
    silver=STARTING_VALUES["Silver"],
    items=[],
)

if __name__ == "__main__":
    print(player)
