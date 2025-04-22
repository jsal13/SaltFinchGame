from saltfinch.common.terminal import slow_print, clear_screen


def start_script():
    clear_screen()
    print("\n" + "=" * 60)
    print("SALT FINCH")
    print("=" * 60)
    slow_print(
        text=[
            "\nYou are a merchant trading goods in the desert state of Graff.",
            "You are trying to make enough money to travel to your family in",
            "the eastern city of Tazir.",
            "\nYou will have to make money by trading goods in the desert,",
            "but be careful: the desert is a dangerous place.",
            "\n\n"
        ],
        delay=0.03,
    )
