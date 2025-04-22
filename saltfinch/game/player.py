from attrs import define

@define
class Player:
    money: float = 1000.0
    inventory: dict[str, int] = {}
