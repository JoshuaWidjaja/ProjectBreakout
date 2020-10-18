import pygame
from random import randint
#Class for the Ball of the game
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

    #Functions below handle movement and speed adjustments for the ball as it is bouncing around the game
    def MoveLeft(self,moveAmount):
        if self.gameBallSpeed == [0,0]:
            self.rect.x -= moveAmount
            if self.rect.x < 30:
                self.rect.x = 30

    def MoveRight(self, moveAmount):
        if self.gameBallSpeed == [0,0]:
            self.rect.x += moveAmount
            if self.rect.x > self.xBoundary - 50:
                self.rect.x = self.xBoundary - 50 

    def InitialBounce(self):
        self.gameBallSpeed[0] = randint(-15,15)
        self.gameBallSpeed[1] = randint(-15, -10)

    def AdjustXSpeed(self):
        self.gameBallSpeed[0] = -self.gameBallSpeed[0]

    def AdjustYSpeed(self):
        self.gameBallSpeed[1] = -self.gameBallSpeed[1]
        
        ##Alternate movement method
        # if self.gameBallSpeed[1] < 0:
        #     self.gameBallSpeed[1] = randint(12,15)
        # elif self.gameBallSpeed[1] > 0:
        #     self.gameBallSpeed[1] = randint(-15, -12)

    def ResetPosition(self, xPosition, yPosition):
        self.rect.x = xPosition
        self.rect.y = yPosition




