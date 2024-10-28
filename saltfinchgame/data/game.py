from saltfinchgame.data.locations import COUNTRIES, TOWNS
from saltfinchgame.data.player import Player
from saltfinchgame.data_structures.game import Game

if __name__ == "__main__":
    game = Game(player=Player, countries=COUNTRIES, towns=TOWNS, current_day=1)
