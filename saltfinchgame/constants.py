from typing import Any

from prompt_toolkit.styles import Style

COLORS: dict[str, str] = {
    "Amber": "#ffc107",
    "Black": "#000000",
    "Blue": "#2196f3",
    "Cyan": "#00bcd4",
    "Deep Orange": "#ff5722",
    "Deep Purple": "#673ab7",
    "Green": "#4caf50",
    "Indigo": "#3f51b5",
    "Light Blue": "#03a9f4",
    "Light Green": "#8bc34a",
    "Lime": "#cddc39",
    "Orange": "#ff9800",
    "Pink": "#e81e63",
    "Purple": "#9c27b0",
    "Red": "#f44336",
    "Teal": "#009688",
    "Yellow": "#ffeb3b",
    "White": "#ffffff",
}

STARTING_VALUES: dict[Any, Any] = {
    "Name": "Jean de Joinville",
    "HP": 100,
    "Silver": 10,
    "Town": "Caerwyn",
    "Country": "Falias",
}

ASCII_MAP_VALUES: dict[Any, Any] = {
    "Width": 50,
    "Height": 20,
    "Symbols": {"Town": "#", "Player": "@", "Background": ".", "Country": "%"},
}

ASCII_STYLES: Style = Style.from_dict(
    {
        "town": COLORS["Purple"],
        "country": COLORS["Pink"],
        "player": COLORS["Blue"],
        "background": COLORS["Light Green"],
        "area-name": COLORS["White"],
        "town": COLORS["Purple"],
    }
)
