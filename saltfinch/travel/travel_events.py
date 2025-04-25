from typing import TYPE_CHECKING


from saltfinch.common.numeric import cast_to_int, cast_to_str

if TYPE_CHECKING:
    from saltfinch.game.player import Player


class TravelEvent:
    def __init__(
        self,
        name: str,
        description: str,
        choices: list[str],
        outcomes: list[dict[str, str | int]],
    ):
        self.name = name
        self.description = description
        self.choices = choices
        # Outcomes format: (health_change, water_change, money_change, message)
        self.outcomes = outcomes

    def occur(self, player: "Player", choice_index: int) -> str:
        outcomes: dict[str, str | int] = self.outcomes[choice_index]

        health_change: int = cast_to_int(outcomes.get("health_change", 0))
        water_change: int = cast_to_int(outcomes.get("water_change", 0))
        message: str = cast_to_str(
            outcomes.get("msg", "You have encountered an event.")
        )

        player.health += health_change
        player.water += water_change

        # Keep values in bounds
        player.health = max(0, min(100, player.health))
        player.water = max(0, min(999, player.water))

        # Check if player has died
        if player.health <= 0:
            player.alive = False
            return f"{message}\n\nYou have died."

        return message
