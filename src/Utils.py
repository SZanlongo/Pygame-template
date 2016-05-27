from pygame.locals import Color


def set_mouse_selection(item, mpos):
    # Marks the MenuItem the mouse cursor hovers on
    if item.is_mouse_selection(mpos):
        item.set_font_color(Color('red'))
        item.set_italic(True)
    else:
        item.set_font_color(Color('white'))
        item.set_italic(False)
