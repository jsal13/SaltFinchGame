from prompt_toolkit.validation import Validator


def is_valid_number(text: str) -> bool:
    """Validate if input is a number."""
    return text is not None and text.isdigit()


# TODO: Can we delete the prompt?
numeric_validator = Validator.from_callable(
    is_valid_number,
    error_message="Input is not a number.",
    move_cursor_to_end=True,
)
