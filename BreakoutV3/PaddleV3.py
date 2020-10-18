import pygame
#Class for the Paddle of the game
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

    #All helper functions below handle movement of the paddle.
    def MoveLeft(self, moveAmount):
        self.rect.x -= moveAmount
        if self.rect.x < 0:
            self.rect.x = 0
        
    def MoveRight(self, moveAmount):
        self.rect.x += moveAmount
        if self.rect.x > self.xBoundary - self.width:
            self.rect.x = self.xBoundary - self.width
    
    def ResetPosition(self, xPosition, yPosition):
        self.rect.x = xPosition
        self.rect.y = yPosition