import pygame


# Block is based on Paul Vincent Craven's tutorial: "Program Arcade Games With Python And Pygame" at:
#  http://programarcadegames.com/index.php
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Block, self).__init__()  # Call the parent class (Sprite) constructor

        # Create an image of the block, and fill it with a color
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # self.image.set_colorkey(Color("white"))  # Transparency

        # Load bit-mapped graphic
        # Removes need for width/height
        # self.image = pygame.image.load("player.png").convert()

        # Rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

    # Update position
    def update(self):
        # # Get the current mouse position
        # # This returns the position as a list of two numbers
        # pos = pygame.mouse.get_pos()
        #
        # # Set the object to the mouse location
        # self.rect.x = pos[0]
        # self.rect.y = pos[1]
        pass
