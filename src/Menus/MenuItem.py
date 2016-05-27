import pygame
from pygame.locals import Color


# MenuItem is based on Nebelhom's tutorial: "Create a simple game menu with pygame" at:
# https://nebelprog.wordpress.com/2013/09/02/create-a-simple-game-menu-with-pygame-pt-4-connecting-it-to-functions/
class MenuItem(pygame.font.Font):
    def __init__(self, text, font=None, font_size=30, font_color=Color('white'), (pos_x, pos_y)=(0, 0)):
        pygame.init()
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y

    def is_mouse_selection(self, (posx, posy)):
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
                (posy >= self.pos_y and posy <= self.pos_y + self.height):
            return True
        else:
            return False

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)
