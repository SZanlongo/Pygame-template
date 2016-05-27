from Block import *


class Agent:
    def __init__(self, uid, environment, layers, color, width, height):
        self.uid = uid  # Unique ID
        self.environment = environment
        self.layers = layers
        self.block = Block(color, width, height)  # Block sprite

    def within_bounds(self):
        return self.environment.within_bounds(self.block)

    def collide_with_obstacle(self):
        return self.environment.collides_with_obstacle(self.block, self.layers)
