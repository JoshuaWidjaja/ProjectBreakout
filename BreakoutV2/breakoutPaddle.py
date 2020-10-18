import pygame

PADDLE_COLOR = (152,160,151)
#PADDLE_X_LIMIT = SCREEN_RESOLUTION[0] - PADDLE_WIDTH

class Paddle():
    def __init__(self, color,  width, height,gameScreenX):
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.paddleXLim = gameScreenX
        self.paddleDim = pygame.Rect(500, 650, width, height)
        #pygame.draw.rect(self.image, self.color, self.paddleDim)


    def moveLeft(self, moveAmount):
        self.paddleDim.left -= moveAmount
        if self.paddleDim.left <= 0:
            self.paddleDim.left = 0

    def moveRight(self, moveAmount):
        self.paddleDim.right += moveAmount
        if self.paddleDim.right > self.paddleXLim:
            self.paddleDim.right = self.paddleXLim
