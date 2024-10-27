from attrs import define, field

from saltfinchgame.constants import ASCII_MAP_VALUES
from saltfinchgame.data_structures.locations import (
    Country,
    CountryList,
    Town,
    TownList,
)


@define()
class MapASCII:
    """ASCII Map object."""

    width: int = field(default=ASCII_MAP_VALUES["Width"])
    height: int = field(default=ASCII_MAP_VALUES["Height"])

    # Available Symbols:
    # 'Town', 'Player', 'Background', 'Country'
    symbols: dict[str, str] = field(default=ASCII_MAP_VALUES["Symbols"])
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
