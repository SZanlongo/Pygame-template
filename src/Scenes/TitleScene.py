from GameScene import *


# TitleScene is based on Blake O'Hare's tutorial: "PyGame Basics Tutorial" at:
# http://www.nerdparadise.com/tech/python/pygame/basics/
class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene())

    # game logic
    def Update(self):
        pass

    # render code
    def Render(self, screen):  # receive the main screen Surface as input
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill(Color("red"))
