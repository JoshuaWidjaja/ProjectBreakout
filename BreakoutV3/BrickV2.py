import pygame


class Brick(pygame.sprite.Sprite):
    def __init__(self, color, xPoint, yPoint, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.width = width
        self.height = height

        self.rect = self.image.get_rect()
        self.rect.x = xPoint 
        self.rect.y = yPoint