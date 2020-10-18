import pygame

print(pygame.ver)

#Constants for the game
SCREEN_RESOLUTION = (1000,700)

PADDLE_X_LOC = 500
PADDLE_Y_LOC = SCREEN_RESOLUTION[1] - 50
PADDLE_HEIGHT = 15
PADDLE_WIDTH = 80
PADDLE_COLOR = (152,160,151)
PADDLE_X_LIMIT = SCREEN_RESOLUTION[0] - PADDLE_WIDTH


GAMEBALL_DIAMETER = 20
GAMEBALL_RADIUS = int(GAMEBALL_DIAMETER/2)
GAMEBALL_X_LOC = int(PADDLE_X_LOC + PADDLE_WIDTH/2)
GAMEBALL_Y_LOC = int(PADDLE_Y_LOC - GAMEBALL_DIAMETER + GAMEBALL_RADIUS)
GAMEBALL_COLOR = (255,255,255)
GAMEBALL_X_LIMIT = SCREEN_RESOLUTION[0] - GAMEBALL_DIAMETER
GAMEBALL_Y_LIMIT = SCREEN_RESOLUTION[1] - GAMEBALL_DIAMETER

BRICK_HEIGHT = 20
BRICK_WIDTH = 80

BRICK_COLOR = (52,183,56)

#Events
new_game_start_event = pygame.USEREVENT
ongoing_game_event = pygame.USEREVENT +1

pygame.time.set_timer(new_game_start_event,100)

class BreakoutGame():
    def __init__(self):
        self.gameScreen = pygame.display.set_mode(SCREEN_RESOLUTION)
        
        self._isRunning = True
        self.playerLives = 3
        self.playerScore = 0
        self.gameballSpeed = [0,0]

        self._createInitialObjects()
    
    def runGame(self):
        pygame.init()
        self._resizeSurface(SCREEN_RESOLUTION)
        self.gameClock = pygame.time.Clock()
        while self._isRunning:
            self.gameClock.tick(150)
            self._eventHandler()
            self._redrawObjects()


        pygame.quit()

    def _resizeSurface(self, size):
        pygame.display.set_mode(size, pygame.RESIZABLE)

    def _createInitialObjects(self):
        self.paddle = pygame.Rect(PADDLE_X_LOC, PADDLE_Y_LOC, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.gameBall  = pygame.Rect(PADDLE_X_LOC + int(PADDLE_WIDTH/2), PADDLE_Y_LOC, GAMEBALL_DIAMETER, GAMEBALL_DIAMETER)
        self.bricks = []

        BRICK_Y_SPACING = 10
        for i in range(8):
            BRICK_X_SPACING = 100
            for j in range(9):
                self.bricks.append(pygame.Rect(BRICK_X_SPACING, BRICK_Y_SPACING, BRICK_WIDTH, BRICK_HEIGHT))
                BRICK_X_SPACING += BRICK_WIDTH + 10
            BRICK_Y_SPACING += BRICK_HEIGHT + 20

    def _redrawObjects(self):
        surface = pygame.display.get_surface()      
        surface.fill(pygame.Color(5,5,5))
        pygame.draw.rect(self.gameScreen, PADDLE_COLOR, self.paddle)
        pygame.draw.circle(self.gameScreen, GAMEBALL_COLOR, (self.gameBall.left, self.gameBall.top - GAMEBALL_RADIUS), GAMEBALL_RADIUS)
        for bricks in self.bricks:
            pygame.draw.rect(self.gameScreen, BRICK_COLOR, bricks)
        pygame.display.flip()


    def _eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._isRunning = False
            elif event.type == pygame.VIDEORESIZE:
                self._resizeSurface(event.size)
            elif event.type == new_game_start_event:
                pass
            elif event.type == ongoing_game_event:
                self.gameBall.left += self.gameballSpeed[0]
                self.gameBall.top += self.gameballSpeed[1]
                if self.gameBall.left >= GAMEBALL_X_LIMIT:
                    self.gameBall.left = GAMEBALL_X_LIMIT
                    self.gameballSpeed[0] = -self.gameballSpeed[0]
                if self.gameBall.top <= 0:
                    self.gameBall.top = 0
                    self.gameballSpeed[1] = -self.gameballSpeed[1]
                if self.gameBall.left <= 0:
                    self.gameBall.left = 0
                    self.gameballSpeed[0] = -self.gameballSpeed[0]
                if self.gameBall.top == SCREEN_RESOLUTION[1]:
                    pass
                for brick in self.bricks:
                    if self.gameBall.colliderect(brick):
                        self.gameballSpeed[1] = -self.gameballSpeed[1]
                        self.bricks.remove(brick)
                if self.gameBall.colliderect(self.paddle):
                    self.gameballSpeed[1] = -self.gameballSpeed[1]
                    
        self._keyHandler()
    
    def _keyHandler(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.gameballSpeed == [0,0]:
            self.gameballSpeed = [15, -15]
            pygame.time.set_timer(ongoing_game_event,100)

        if keys[pygame.K_LEFT] and self.gameballSpeed != [0,0]:
            self.paddle.left -= 5

            if self.gameballSpeed == [0,0]:
                self.gameBall.left -= 5
            if self.paddle.left < 0:
                self.paddle.left = 0
        
        if keys[pygame.K_RIGHT] and self.gameballSpeed != [0,0]:
            self.paddle.left += 5
            if self.gameballSpeed == [0,0]:
                self.gameBall.left += 5
            if self.paddle.right > PADDLE_X_LIMIT:
                self.paddle.right = PADDLE_X_LIMIT

      


if __name__ == "__main__":
    BreakoutGame().runGame()    