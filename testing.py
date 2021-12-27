import pygame
import random
import pygame as pg
from pygame.locals import *
from pygame import Surface

pygame.init()

running = True
screen = pygame.display.set_mode((800, 600))
ballIMG = pygame.image.load('ball.png')
pygame.display.set_caption('PONG')
pygame.display.set_icon(ballIMG)
iY = 300
fY = random.randint(0, 600)
iX = 400
fX = 0
px = 10
py = 300
ex = 770
ey = 300
pYspeed = 2
counter = 0

balldir = 'left'


# ball
def ball(x, y):
    ball = pygame.Rect(x, y, 32, 32)
    screen.blit(ballIMG, ball)


while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    startV = pygame.Vector2(iX, iY)
    finalV = pygame.Vector2(fX, fY)

    if counter < 500:
        progress = counter / 500
        currentV = startV.lerp(finalV, progress)
        counter += 1

    player_rect = Rect(px, py, 20, 100)
    enem_rect = Rect(ex, ey, 20, 100)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and py > 0:
        py -= pYspeed
    if keys[pygame.K_DOWN] and py < 600 - 100:
        py += pYspeed


    pygame.draw.rect(screen, (255, 255, 255), player_rect)
    pygame.draw.rect(screen, (255, 255, 255), enem_rect)
    screen.blit(ballIMG, currentV)
    pygame.display.update()
