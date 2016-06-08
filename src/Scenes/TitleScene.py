from GameScene import *


# TitleScene is based on Blake O'Hare's tutorial: "PyGame Basics Tutorial" at:
# http://www.nerdparadise.com/tech/python/pygame/basics/part7/
class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.bg_color = Color('red')

    def ProcessInput(self, events, pressed_keys, mpos):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene())

    # game logic
    def Update(self):
        pass

    # render code
    def Render(self, screen):  # receive the main screen Surface as input
        # Redraw the background
        screen.fill(self.bg_color)
