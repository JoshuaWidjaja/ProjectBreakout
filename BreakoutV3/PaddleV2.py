import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, xPoint, yPoint, width, height, xBoundary):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.width = width
        self.xBoundary = xBoundary
        
        self.rect = self.image.get_rect()
        self.rect.x = xPoint 
        self.rect.y = yPoint

    
    def moveLeft(self, moveAmount):
        self.rect.x -= moveAmount
        if self.rect.x < 0:
            self.rect.x = 0
        
    def moveRight(self, moveAmount):
        self.rect.x += moveAmount
        if self.rect.x > self.xBoundary - self.width:
            self.rect.x = self.xBoundary - self.width
    
    def resetPosition(self, xPosition, yPosition):
        self.rect.x = xPosition
        self.rect.y = yPosition