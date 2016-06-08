import heapq

from pygame.locals import Color


# PriorityQueue is based on Amit Patel's tutorial: "Implementation of A*" at:
# http://www.redblobgames.com/pathfinding/a-star/implementation.html
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def set_mouse_selection(item, mpos):
    # Marks the MenuItem the mouse cursor hovers on
    if item.is_mouse_selection(mpos):
        item.set_font_color(Color('red'))
        item.set_italic(True)
    else:
        item.set_font_color(Color('white'))
        item.set_italic(False)
