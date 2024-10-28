from saltfinchgame.data_structures.trader import Trader


def test_trader_initializes(item_fixture):
    Trader(name="Testy Boi", items=item_fixture)
