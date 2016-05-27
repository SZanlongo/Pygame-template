import sys

import src.Globals as gb
from src.Menus.MenuItem import *
from src.Scenes.GameScene import *
from src.Utils import *


# MenuScene is based on Nebelhom's tutorial: "Create a simple game menu with pygame" at:
# https://nebelprog.wordpress.com/2013/09/02/create-a-simple-game-menu-with-pygame-pt-4-connecting-it-to-functions/
class MenuScene(SceneBase):
    def __init__(self, funcs, font=None, font_size=30, font_color=Color('white')):
        SceneBase.__init__(self)
        self.bg_color = Color('black')

        self.funcs = funcs
        funcs['Start'] = self.next_scene
        funcs['Quit'] = sys.exit
        items = funcs.keys()
        self.items = []
        for index, item in enumerate(items):
            menu_item = MenuItem(item, font, font_size, font_color)

            t_h = len(items) * menu_item.height  # total height of text block
            pos_x = (gb.WINDOW_WIDTH / 2) - (menu_item.width / 2)
            pos_y = (gb.WINDOW_HEIGHT / 2) - (t_h / 2) + ((index * 2) + index * menu_item.height)

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)

        self.mouse_is_visible = True
        self.cur_item = None

        self.mpos = None

    def next_scene(self):
        self.SwitchToScene(GameScene())

    def set_keyboard_selection(self, key):
        # Mark the MenuItem chosen via up and down keys
        for item in self.items:
            # Return all to neutral
            item.set_italic(False)
            item.set_font_color(Color('white'))

        if self.cur_item is None:
            self.cur_item = 0
        else:
            # Find the chosen item
            if key == pygame.K_UP and self.cur_item > 0:
                self.cur_item -= 1
            elif key == pygame.K_UP and self.cur_item == 0:
                self.cur_item = len(self.items) - 1
            elif key == pygame.K_DOWN and self.cur_item < len(self.items) - 1:
                self.cur_item += 1
            elif key == pygame.K_DOWN and self.cur_item == len(self.items) - 1:
                self.cur_item = 0

        self.items[self.cur_item].set_italic(True)
        self.items[self.cur_item].set_font_color(Color('red'))

        # Finally check if Enter or Space is pressed
        if key == pygame.K_SPACE or key == pygame.K_RETURN:
            text = self.items[self.cur_item].text
            self.funcs[text]()

    def ProcessInput(self, events, pressed_keys, mpos):
        self.mpos = mpos

        for event in events:
            if event.type == pygame.KEYDOWN:
                self.mouse_is_visible = False
                self.set_keyboard_selection(event.key)
            if event.type == pygame.MOUSEBUTTONDOWN:
                for item in self.items:
                    if item.is_mouse_selection(mpos):
                        self.funcs[item.text]()

        if pygame.mouse.get_rel() != (0, 0):
            self.mouse_is_visible = True
            self.cur_item = None

        pygame.mouse.set_visible(self.mouse_is_visible)

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill(self.bg_color)

        if self.mouse_is_visible:
            for item in self.items:
                set_mouse_selection(item, self.mpos)
                screen.blit(item.label, item.position)
