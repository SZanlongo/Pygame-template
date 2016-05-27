from src.Menus.MenuScene import *
from src.Scenes.Game import *


def main():
    # Run game
    funcs = {}

    run_game(gb.WINDOW_WIDTH, gb.WINDOW_HEIGHT, gb.FPS, gb.WINDOW_CAPTION, MenuScene(funcs))


if __name__ == "__main__":
    main()
