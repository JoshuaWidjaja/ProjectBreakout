import pygame
from breakoutPaddle import Paddle
from breakoutBall import GameBall
from breakoutBrick import Brick

print(pygame.ver)

SCREEN_RESOLUTION = (1000,700)
isRunning = False
#Colors
PADDLE_COLOR = (152,160,151)
GAMEBALL_COLOR = (255,255,255)
BRICK_COLOR1 = (52,183,56)


#Events
new_game_start_event = pygame.USEREVENT
ongoing_game_event = pygame.USEREVENT +1

pygame.time.set_timer(new_game_start_event,100)

def runGame():
    gameScreen = pygame.display.set_mode(SCREEN_RESOLUTION)
    isRunning = True
    livesCount = 3
    playerScore = 0

    paddle = Paddle(PADDLE_COLOR, 80, 15, SCREEN_RESOLUTION[0])
    gBall = GameBall(GAMEBALL_COLOR, 10, SCREEN_RESOLUTION[0], SCREEN_RESOLUTION[1])
    brickList = list()
    BRICK_Y = 10
    for i in range(8):
        BRICK_X = 100
        for j in range(9):
            brick = Brick(BRICK_X, BRICK_Y, BRICK_COLOR1, 80, 20)
            brickList.append(brick.brickDim)
            BRICK_X += brick.width + 10
        BRICK_Y += brick.height + 20
    gameClock = pygame.time.Clock()

    while isRunning:
            gameClock.tick(90)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isRunning = False
                elif event.type == new_game_start_event:
                    pass
                elif event.type == ongoing_game_event:
                    gBall.gameBallDim.left += gBall.gameBallSpeed[0]
                    gBall.gameBallDim.top += gBall.gameBallSpeed[1]
                    if gBall.gameBallDim.left >= SCREEN_RESOLUTION[0] - gBall.radius*2:
                        gBall.gameBallDim.left = SCREEN_RESOLUTION[0] - gBall.radius*2
                        gBall.gameBallSpeed[0] = -gBall.gameBallSpeed[0]
                    if gBall.gameBallDim.top <= 0:
                        gBall.gameBallDim.top = 0
                        gBall.gameBallSpeed[1] = -gBall.gameBallSpeed[1]
                    if gBall.gameBallDim.left <= 0:
                        gBall.gameBallDim.left = 0
                        gBall.gameBallSpeed[0] = -gBall.gameBallSpeed[0]
                    if gBall.gameBallDim.top == SCREEN_RESOLUTION[1]:
                        pass
                    for brickDim in brickList:
                         if gBall.gameBallDim.colliderect(brickDim):
                            gBall.gameBallSpeed[1] = -gBall.gameBallSpeed[1]
                            brickList.remove(brickDim)
                    if paddle.paddleDim.colliderect(gBall.gameBallDim):
                        gBall.gameBallSpeed[1] = -gBall.gameBallSpeed[1]
                    #if gBall.gameBallDim.colliderect(paddle.paddleDim):
                    #    gBall.gameBallSpeed[1] = -gBall.gameBallSpeed[1]
            redrawObjects(gameScreen,paddle,gBall,brickList)
            keyHandler(paddle,gBall)

    pygame.quit()




def redrawObjects(screen,paddle,ball,brickList):
    surface = pygame.display.get_surface()      
    surface.fill(pygame.Color(5,5,5))
    pygame.draw.rect(screen, PADDLE_COLOR, paddle.paddleDim)
    pygame.draw.circle(screen, GAMEBALL_COLOR, (ball.gameBallDim.left + int(paddle.width/2), ball.gameBallDim.top - ball.radius), ball.radius)
    for brickDims in brickList:
        pygame.draw.rect(screen, BRICK_COLOR1, brickDims)
    pygame.display.flip()

def keyHandler(paddle,ball):
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_SPACE] and ball.gameBallSpeed == [0,0]:
        ball.gameBallSpeed = [15, -15]
        pygame.time.set_timer(ongoing_game_event,100)
    if keys[pygame.K_LEFT] and ball.gameBallSpeed != [0,0]:
            paddle.moveLeft(5)
            #ball.moveLeft(5)
    if keys[pygame.K_LEFT] and ball.gameBallSpeed == [0,0]:
            paddle.moveLeft(5)
            ball.moveLeft(5)
    if keys[pygame.K_RIGHT] and ball.gameBallSpeed != [0,0]:
            paddle.moveRight(5)
            #ball.moveRight(5)
    if keys[pygame.K_RIGHT] and ball.gameBallSpeed == [0,0]:
            paddle.moveRight(5)
            ball.moveRight(5)
if __name__ == "__main__":
    runGame()