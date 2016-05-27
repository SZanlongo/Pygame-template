# SceneBase is based on Blake O'Hare's tutorial: "PyGame Basics Tutorial" at:
# http://www.nerdparadise.com/tech/python/pygame/basics/
class SceneBase:
    def __init__(self):
        self.next = self  # Next scene

    # receive all the events that happened since the last frame
    def ProcessInput(self, events, pressed_keys, mpos):
        print("uh-oh, you didn't override this in the child class")

    # game logic
    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    # render code
    def Render(self, screen):  # receive the main screen Surface as input
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)
