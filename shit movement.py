import pygame
import random
from pygame.locals import *
from pygame import mixer

pygame.init()

running = True
screen = pygame.display.set_mode((800, 600))
ballIMG = pygame.image.load('ball.png')
pygame.display.set_caption('PONG')
pygame.display.set_icon(ballIMG)


Y = random.randint(32, 600 - 32)
rightX = 800 - 32
leftX = 0
ballX = 368
ballY = 268
Xspeed = 1
# making Yspeed lower makes it appear as if it moves diagonally but not always
Yspeed = 0.3
eyspeed = 0.2
pYspeed = 2
balldir = 'right'
px = 10
py = 300
ex = 770
ey = 300
boing = mixer.Sound('mixkit-arcade-game-jump-coin-216.wav')
scoresfx = mixer.Sound('mixkit-arcade-bonus-alert-767.wav')
lose = mixer.Sound('mixkit-retro-arcade-game-over-470.wav')
game_over_text = pygame.font.Font('freesansbold.ttf', 70)
scoretxt = pygame.font.Font('freesansbold.ttf', 32)
score_value = 0


def show_score(x, y):
    score = scoretxt.render(str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over(x, y):
    fontgameover = game_over_text.render('GAME OVER', True, (255, 255, 255))
    screen.blit(fontgameover, (x, y))


# ball
def ball(x, y):
    ballcharaf = pygame.Rect(x, y, 32, 32)
    screen.blit(ballIMG, ballcharaf)


while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ballchara = pygame.Rect(ballX, ballY, 32, 32)
    player_rect = Rect(px, py, 20, 100)
    enem_rect = Rect(ex, ey, 20, 100)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and py > 0:
        py -= pYspeed
    if keys[pygame.K_DOWN] and py < 600 - 100:
        py += pYspeed

    if ballY < Y:
        ballY += Yspeed
    elif ballY > Y:
        ballY -= Yspeed

    if balldir == 'right':
        if pygame.Rect.colliderect(enem_rect, ballchara):
            boing.play()
            print('r')
            balldir = 'left'
            Y = random.randint(32, 600 - 32)
        if ballX // 1 == rightX:
            scoresfx.play()
            score_value += 1
            ballX, ballY = 368, 268
        if ballX < rightX:
            ballX += Xspeed
    if balldir == 'left':
        if pygame.Rect.colliderect(player_rect, ballchara):
            boing.play()
            print('e')
            balldir = 'right'
            Y = random.randint(32, 600 - 32)
        if ballX // 1 == leftX:
            print('e')
            lose.play()
            balldir = 'break'
        if ballX > leftX:
            ballX -= Xspeed
    if balldir == 'break':
        game_over(190, 250)
        ballX = 400
        ballY = 2000

    if ey > ballY - 32 and ey > 0:
        ey -= eyspeed
    if ey < ballY - 32 and ey < 500:
        ey += eyspeed

    show_score(400, 10)
    pygame.draw.rect(screen, (255, 255, 255), player_rect)
    pygame.draw.rect(screen, (255, 255, 255), enem_rect)
    ball(ballX, ballY)
    pygame.display.update()
