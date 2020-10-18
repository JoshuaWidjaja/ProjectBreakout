import pygame

GAMEBALL_COLOR = (255,255,255)

class GameBall():
    def __init__(self, color, radius,gamescreenX, gamescreenY):
        self.color = color
        self.radius = radius
        self.ballXLim = gamescreenX
        self.ballYLim = gamescreenY
        self.image = pygame.Surface([radius, radius])
        self.gameBallSpeed = [0,0]
        self.gameBallDim = pygame.Rect(500 , gamescreenY-50, self.radius, self.radius)
        #pygame.draw.circle(self.image, GAMEBALL_COLOR, (self.gameballDim.left, self.gameballDim.top - self.radius), self.radius)

    def moveLeft(self,moveAmount):
        if self.gameBallSpeed == [0,0]:
            self.gameBallDim.left -= moveAmount
            if self.gameBallDim.left < 0:
                self.gameBallDim.left = 0

    def moveRight(self, moveAmount):
        if self.gameBallSpeed == [0,0]:
            self.gameBallDim.left += moveAmount
            if self.gameBallDim.right > self.ballXLim - 70:
                self.gameBallDim.right = self.ballXLim - 70 
