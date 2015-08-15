# Main game file
import pygame
import random
from player import Player
from stair import *
from config import *
import levelInit

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("DonkeyKong")

screen.fill((255, 255, 255))

levelInit.commonInit(screen)

# Initialize level
for i in range(200,800,70):
    pygame.draw.line(screen, (255,0,255) , (1, i), (WIDTH-1, i), 2)
    pygame.draw.line(screen, (255,0,255) , (1, i+4), (WIDTH-1, i+4), 2)

done = False

hero = Player()
hero_group = pygame.sprite.GroupSingle(hero.makePlayer())


#stair_group = pygame.sprite.OrderedUpdates()
#broken_stair_group = pygame.sprite.OrderedUpdates()

#for i in range(8):
#    stair = Stair("Complete").makeStair()
#    stair.rect.left = random.randint(1,NUM_TILES_WIDTH-1) * TILE_SIZE
#    stair.rect.top =  204 + i*70
#    stair_group.add(stair)

addStairs(screen)
addBrokenStairs(screen)

while done == False :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            done = True
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_q:
                done = True
            elif event.key == pygame.K_w or event.key == pygame.K_UP :
                hero.moveUP(screen)
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN :
                hero.moveDown(screen)
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT :
                hero.moveLeft(screen)
                print "Left"
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT :
                hero.moveRigth(screen)
                print "RIght"
    hero_group.draw(screen)
    #stair_group.draw(screen)
    pygame.display.update()

pygame.quit()
