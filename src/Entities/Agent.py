from Block import *


# Define an entity in the game with unique behaviors
class Agent:
    def __init__(self, uid, environment, layers, sight, color, width, height):
        self.uid = uid  # Unique ID
        self.environment = environment  # environment the agent is inside of (reference)
        self.sight = 1  # how far the agent can "see"
        self.path = None  # trajectory
        self.block = Block(color, width, height)  # Block sprite
