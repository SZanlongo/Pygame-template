import pygame
from pygame.locals import Color

from SceneBase import *


# GameScene is based on Blake O'Hare's tutorial: "PyGame Basics Tutorial" at:
# http://www.nerdparadise.com/tech/python/pygame/basics/
class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.bg_color = Color('blue')

        # List of every sprite
        self.all_sprites_list = pygame.sprite.Group()

    # receive all the events that happened since the last frame
    def ProcessInput(self, events, pressed_keys, mpos):
        pass

    # game logic
    def Update(self):
        pass

    # render code
    def Render(self, screen):  # receive the main screen Surface as input
        # Redraw the background
        screen.fill(self.bg_color)

        # Draw all the spites
        self.all_sprites_list.draw(screen)
