from pygame.locals import Color

from GameScene import *
from src.Menus.MenuItem import *


class MenuScene(SceneBase):
    def __init__(self, screen, items, funcs,
                 bg_color=Color('black'), font=None, font_size=30, font_color=Color('black')):
        SceneBase.__init__(self)
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

        self.bg_color = bg_color
        self.clock = pygame.time.Clock()

        self.funcs = funcs
        self.items = []
        for index, item in enumerate(items):
            menu_item = MenuItem(item, font, font_size, font_color)

            t_h = len(items) * menu_item.height  # total height of text block
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)
            pos_y = (self.scr_height / 2) - (t_h / 2) + ((index * 2) + index * menu_item.height)

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)

        self.mouse_is_visible = True
        self.cur_item = None

    def set_keyboard_selection(self, key):
        # Marks the MenuItem chosen via up and down keys
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

    def set_mouse_selection(self, item, mpos):
        # Marks the MenuItem the mouse cursor hovers on
        if item.is_mouse_selection(mpos):
            item.set_font_color(Color('red'))
            item.set_italic(True)
        else:
            item.set_font_color(Color('white'))
            item.set_italic(False)

    def ProcessInput(self, events, pressed_keys, mpos):
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

    # game logic
    def Update(self):
        pass

    # render code
    def Render(self, screen):  # receive the main screen Surface as input
        # Redraw the background
        screen.fill(self.bg_color)
