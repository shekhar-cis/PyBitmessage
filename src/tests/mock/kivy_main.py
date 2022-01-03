"""Mock kivy app with mock threads."""


"""This module is for thread start."""
from pybitmessage import state

if __name__ == '__main__':
    state.kivy = True
    print("Kivy Loading......")
    from bitmessagemock import main
    main()
