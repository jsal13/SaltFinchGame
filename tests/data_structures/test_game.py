from saltfinchgame.data_structures.game import Game


def test_game_initializes(player_fixture, countrylist_fixture, townlist_fixture):
    assert Game(
        player=player_fixture, countries=countrylist_fixture, towns=townlist_fixture
    )
