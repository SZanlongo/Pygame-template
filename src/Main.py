from src.menus.MenuScene import *
from src.scenes.Game import *


def main():
    # Run game
    funcs = {}

    run_game(gb.WINDOW_WIDTH, gb.WINDOW_HEIGHT, gb.FPS, gb.WINDOW_CAPTION, MenuScene(funcs))


if __name__ == "__main__":
    main()
