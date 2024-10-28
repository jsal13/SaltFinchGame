from attrs import define, field, validators

from saltfinchgame.data_structures.locations import (
    Country,
    CountryList,
    Town,
    TownList,
)


@define()
class MapLocation:
    """Location on the ASCII Map."""

    x: int = field(default=0, validator=validators.ge(0))
    y: int = field(default=0, validator=validators.ge(0))

    def __iter__(self):
        return iter((self.x, self.y))


@define()
class MapASCII:
    """ASCII Map object."""

    width: int
    height: int
    symbols: dict[str, str]
    map_grid: list[list[str]] = field(init=False)

    def _generate_map_grid_base_layer(self) -> None:
        self.map_grid = [
            list(self.symbols["Background"] * self.width) for _ in range(self.height)
        ]

    def _generate_area_locations(self, areas: CountryList | TownList) -> None:
        """Generate town or country locations on the map."""
        if self.map_grid is None:
            msg: str = "`map_grid` has not been initialized."
            raise Exception(msg)

        for area in areas:
            x, y = area.map_location

            if isinstance(area, Town):
                self.map_grid[y][x] = self.symbols["Town"]
            elif isinstance(area, Country):
                self.map_grid[y][x] = self.symbols["Country"]
            else:
                msg: str = "`area` is not a `Town` or `Country`."
                raise Exception(msg)

            for n, letter in enumerate(area.name.name):
                self.map_grid[y + 1][x + n - 2] = letter
