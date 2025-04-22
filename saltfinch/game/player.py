from attrs import define


@define
class Player:
    health: int = 100
    water: int = 20
    money: float = 1000.0
    inventory: dict[str, int] = {}
    alive: bool = True
    is_in_town: bool = True
    is_traveling: bool = False

    def __str__(self) -> str:
        return (
            f"Player(health={self.health}, water={self.water}, "
            f"money={self.money}, inventory={self.inventory}, "
            f"alive={self.alive}, is_in_town={self.is_in_town}, "
            f"is_traveling={self.is_traveling})"
        )
