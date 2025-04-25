"""
Functions to cast values to numeric types.
"""

from typing import Any


def cast_to_int(value: Any) -> int:
    """
    Cast a value to an integer, handling None and empty strings.
    """
    if value is None or value == "":
        return 0
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0


def cast_to_float(value: Any) -> float:
    """
    Cast a value to a float, handling None and empty strings.
    """
    if value is None or value == "":
        return 0.0
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0


def cast_to_str(value: Any) -> str:
    """
    Cast a value to a string, handling None and empty strings.
    """
    if value is None:
        return ""
    try:
        return str(value)
    except (ValueError, TypeError):
        return ""


def cast_to_bool(value: Any) -> bool:
    """
    Cast a value to a boolean, handling None and empty strings.
    """
    if value is None or value == "":
        return False
    try:
        return bool(value)
    except (ValueError, TypeError):
        return False
