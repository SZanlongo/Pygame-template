import pygame


class Environment():
    def __init__(self, boundaries):
        self.boundaries = boundaries
        self.obstacles = {}

    def within_bounds(self, block):
        if block.rect.x < self.boundaries['left'] or \
                                block.rect.x + block.rect.get_width > self.boundaries['right'] or \
                        block.rect.y < self.boundaries['top'] or \
                                block.rect.y + block.get_height > self.boundaries['bottom']:
            return False
        else:
            return True

    def collides_with_obstacle(self, block, layers):
        for layer in layers:
            if pygame.sprite.spritecollideany(block, self.obstacles[layer], False):
                return True
        return False
