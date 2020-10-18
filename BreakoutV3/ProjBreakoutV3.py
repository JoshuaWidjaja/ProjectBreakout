import pygame
from PaddleV2 import Paddle
from BallV2 import GameBall
from BrickV2 import Brick
from random import randint

print(pygame.ver)

SCREEN_RESOLUTION = (1000,700)
isRunning = False

#Colors
FONT_COLOR = (255,255,255)
PADDLE_COLOR = (152,160,151)
GAMEBALL_COLOR = (255,255,255)
BRICK_COLOR1 = (52,183,56)
BRICK_COLOR2 = (251, 30, 20)
BRICK_COLOR3 = (20, 118, 251)

#Events
new_game_start_event = pygame.USEREVENT
ongoing_game_event = pygame.USEREVENT +1  
pygame.time.set_timer(new_game_start_event,100)

def runGame():
    #Initializing variables and setting up sprites for game.
    gameScreen = pygame.display.set_mode(SCREEN_RESOLUTION)
    surface = pygame.display.get_surface()    
    isRunning = True
    livesCount = 3
    playerScore = 0
    gameClock = pygame.time.Clock()
    
    spriteList = pygame.sprite.Group()
    brickList = pygame.sprite.Group()
    paddle = Paddle(PADDLE_COLOR, 460, 650, 80, 20, SCREEN_RESOLUTION[0])
    spriteList.add(paddle)
    gameball = GameBall(GAMEBALL_COLOR, 490, (SCREEN_RESOLUTION[1] - 70), 6.5, SCREEN_RESOLUTION[0])
    spriteList.add(gameball)

    #Creating bricks for the game
    brickY = 10
    for i in range(3):
        brickX = 100
        for j in range(9):
            brick = Brick(BRICK_COLOR1, brickX, brickY, 80, 15)
            spriteList.add(brick)
            brickList.add(brick)
            brickX = brickX + brick.width + 10
        brickY = brickY + brick.height + 10
    for i in range(3):
        brickX = 100
        for j in range(9):
            brick = Brick(BRICK_COLOR2, brickX, brickY, 80, 15)
            spriteList.add(brick)
            brickList.add(brick)
            brickX = brickX + brick.width + 10
        brickY = brickY + brick.height + 10
    for i in range(3):
        brickX = 100
        for j in range(9):
            brick = Brick(BRICK_COLOR3, brickX, brickY, 80, 15)
            spriteList.add(brick)
            brickList.add(brick)
            brickX = brickX + brick.width + 10
        brickY = brickY + brick.height + 10

    #Main Game loop
    while isRunning:
            gameClock.tick(90) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isRunning = False
                elif event.type == new_game_start_event:
                    pass
                elif event.type == ongoing_game_event:
                    gameball.rect.x += gameball.gameBallSpeed[0]
                    gameball.rect.y += gameball.gameBallSpeed[1]
                    if gameball.rect.x >= SCREEN_RESOLUTION[0] - gameball.radius*2:
                        gameball.rect.x = SCREEN_RESOLUTION[0] - gameball.radius*2
                        gameball.gameBallSpeed[0] = -gameball.gameBallSpeed[0]
                    if gameball.rect.y <= 0:
                        gameball.rect.y = 0
                        gameball.adjustYSpeed()
                    if gameball.rect.x <= 0:
                        gameball.rect.x = 0
                        gameball.gameBallSpeed[0] = -gameball.gameBallSpeed[0]
                    if gameball.rect.y >= (SCREEN_RESOLUTION[1] - 10):
                        livesCount -= 1
                        gameball.gameBallSpeed = [0,0]
                        paddle.resetPosition(460, 650)
                        gameball.resetPosition(490, (SCREEN_RESOLUTION[1] - 70))
                    if pygame.sprite.collide_rect(paddle, gameball):
                        gameball.adjustXSpeed()
                        gameball.adjustYSpeed()
                    for brick in brickList:
                         if pygame.sprite.collide_rect(gameball, brick):
                            gameball.adjustYSpeed()
                            brick.kill()
                            playerScore += 10
            if livesCount == 0:
                font = pygame.font.Font(None, 100)
                endText = font.render("GAME OVER", 1, FONT_COLOR)
                surface.blit(endText, (400,400))
                pygame.display.flip()
                pygame.time.wait(6000)
                isRunning = False
            redrawObjects(surface,spriteList,playerScore, livesCount)
            keyHandler(paddle, gameball)
    pygame.quit()



def redrawObjects(surface,spriteList,playerScore, playerLives):     
    surface.fill(pygame.Color(5,5,5))
    spriteList.update()
    font = pygame.font.Font(None, 28)
    scoreText = font.render("Score: " + str(playerScore), 1, FONT_COLOR)
    surface.blit(scoreText, (10,675))
    livesText = font.render("Lives: " + str(playerLives), 1, FONT_COLOR)
    surface.blit(livesText, (900, 675))
    spriteList.draw(surface)
    pygame.display.flip()

def keyHandler(paddle,ball):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and ball.gameBallSpeed == [0,0]:
        ball.initialBounce()
        pygame.time.set_timer(ongoing_game_event,100)
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
        ball.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)
        ball.moveRight(5)

if __name__ == "__main__":
    pygame.init()
    runGame()
    