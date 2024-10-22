from prompt_toolkit import HTML, print_formatted_text, prompt
from prompt_toolkit.styles import Style

from saltfinchgame.input_validator import numeric_validator

style = Style.from_dict(
    {
        "aaa": "#ff0066",
        "bbb": "#44ff00 italic",
    }
)


text = prompt(
    "Gimme some lovin': ",
    validator=numeric_validator,
    validate_while_typing=False,
    mouse_support=True,
)
print_formatted_text(HTML(f"<aaa>Hello</aaa> <bbb>{text}</bbb>!"), style=style)
