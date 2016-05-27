import Globals
from src.Scenes.Game import *


def main():
    # Run game
    run_game(Globals.WINDOW_WIDTH, Globals.WINDOW_HEIGHT, Globals.FPS, Globals.WINDOW_CAPTION, TitleScene())


if __name__ == "__main__":
    main()
