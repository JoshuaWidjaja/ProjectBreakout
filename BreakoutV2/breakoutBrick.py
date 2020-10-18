import pygame

class Brick():
    def __init__(self, xSpace, ySpace, color, width, height):
        self.color = color
        self.width = width
        self.height = height
        self.xSpace = xSpace
        self.ySpace = ySpace
        self.image = pygame.Surface([width,height])
        
        self.brickDim = pygame.Rect(xSpace, ySpace, width, height)
        

