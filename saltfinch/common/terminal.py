import os 
import time

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text: str | list[str], delay: float = 0.03):
    if isinstance(text, list):
        text = "\n".join(text)

    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)