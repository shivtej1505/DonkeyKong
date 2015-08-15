# Main game file
import pygame
import random
from player import Player
from config import *
from stair import *
import level

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("DonkeyKong")

# Initialize level

done = False

hero = Player()
hero_group = pygame.sprite.GroupSingle(hero.makePlayer())

while done == False :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            done = True
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_w or event.key == pygame.K_UP :
                hero.moveUP(screen)
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN :
                hero.moveDown(screen)
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT :
                hero.moveLeft(screen)
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT :
                hero.moveRigth(screen)
    level.selectLevel(screen,1)
    hero_group.draw(screen)
    #stair_group.draw(screen)
    pygame.display.update()

pygame.quit()
