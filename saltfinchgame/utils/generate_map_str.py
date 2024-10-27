import copy
import string

from prompt_toolkit import HTML, print_formatted_text

from saltfinchgame.constants import ASCII_MAP_VALUES, ASCII_STYLES


# ASCII MAP Symbols": {"Town": "#", "Player": "@", "Background": ".", "Country": "%"},
def inject_html_into_map(map_grid: list[list[str]]) -> list[list[str]]:
    """Inject html into the map grid to include colors, etc., with Prompt_Toolkit."""
    new_map_grid = copy.deepcopy(map_grid)

    ascii_symbols: dict[str, str] = ASCII_MAP_VALUES["Symbols"]
    for y, row in enumerate(map_grid):
        for x, col in enumerate(row):
            html_tag_name: str
            if col == ascii_symbols["Town"]:
                html_tag_name = "town"
            elif col == ascii_symbols["Country"]:
                html_tag_name = "country"
            elif col == ascii_symbols["Player"]:
                html_tag_name = "player"
            elif col == ascii_symbols["Background"]:
                html_tag_name = "background"
            elif col in string.ascii_letters:
                html_tag_name = "area-name"

            # If the symbol was one of these above values...
            if html_tag_name:
                new_map_grid[y][x] = f"<{html_tag_name}>{col}</{html_tag_name}>"

    return new_map_grid


def return_map_str(map_grid: list[list[str]]) -> HTML:
    """Returns map as ASCII from a `MapASCII.map_grid`."""
    new_map_grid = inject_html_into_map(map_grid=map_grid)
    return HTML("\n".join(["".join(row) for row in new_map_grid]))


def print_map_as_formatted_str(html_map_str: str) -> None:
    """Print a formatted map using the `print_formatted_text` function."""
    print_formatted_text(html_map_str, style=ASCII_STYLES)


if __name__ == "__main__":
    from saltfinchgame.data.countries import COUNTRIES
    from saltfinchgame.data_structures.ascii_map import MapASCII

    towns_in_falias = COUNTRIES.get_by_name("FALIAS").towns
    countries = COUNTRIES

    ma = MapASCII()
    ma._generate_map_grid_base_layer()
    ma._generate_area_locations(areas=towns_in_falias)
    # ma._generate_area_locations(areas=COUNTRIES)
    _map = return_map_str(ma.map_grid)

    print_map_as_formatted_str(_map)
