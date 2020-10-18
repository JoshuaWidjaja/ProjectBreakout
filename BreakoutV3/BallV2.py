import pygame
from random import randint
class GameBall(pygame.sprite.Sprite):
    def __init__(self, color, xPoint, yPoint, radius, xBoundary):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([radius*2, radius*2])
        self.image.fill(color)
        self.gameBallSpeed = [0,0]
        self.radius = radius
        self.xBoundary = xBoundary
        
        self.rect = self.image.get_rect()
        
        self.rect.x = xPoint 
        self.rect.y = yPoint

    def moveLeft(self,moveAmount):
        if self.gameBallSpeed == [0,0]:
            self.rect.x -= moveAmount
            if self.rect.x < 30:
                self.rect.x = 30

    def moveRight(self, moveAmount):
        if self.gameBallSpeed == [0,0]:
            self.rect.x += moveAmount
            if self.rect.x > self.xBoundary - 50:
                self.rect.x = self.xBoundary - 50 

    def initialBounce(self):
        self.gameBallSpeed[0] = randint(-15,15)
        self.gameBallSpeed[1] = randint(-15, -10)

    def adjustXSpeed(self):
        self.gameBallSpeed[0] = -self.gameBallSpeed[0]

    def adjustYSpeed(self):
        if self.gameBallSpeed[1] < 0:
            self.gameBallSpeed[1] = randint(12,15)
        elif self.gameBallSpeed[1] > 0:
            self.gameBallSpeed[1] = randint(-15, -12)

    def resetPosition(self, xPosition, yPosition):
        self.rect.x = xPosition
        self.rect.y = yPosition




