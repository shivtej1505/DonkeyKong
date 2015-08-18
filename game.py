# Main game file
import pygame
import random
import sys
from player import Player
from config import *
from stair import *
from fireball import Fireball
import level

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("DonkeyKong")

    # Initialize level

    done = False

    hero = Player()
    hero_group = pygame.sprite.GroupSingle(hero.makePlayer())
    fireball = Fireball()
    fireball_group = pygame.sprite.GroupSingle(fireball.makeFireball())
    pygame.key.set_repeat(8,10)
    while done == False :
        level.selectLevel(screen,1)
        hero_group.draw(screen)
        #fireball_group.draw(screen)
        pygame.display.update()
        #collision = pygame.sprite.groupcollide(hero_group, level.getGroup(),False,True)
        #print collision
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                done = True
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    done = True
                elif event.key == pygame.K_w or event.key == pygame.K_UP :
       #             if len(collision) > 0:
       #                 print "up"
                    hero.moveUP(screen,hero_group,level.getStairGroup())
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN :
        #            if len(collision) > 0:
         #              print "down"
                    hero.moveDown(screen,hero_group,level.getStairGroup())
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT :
                    hero.moveLeft(screen)
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT :
                    hero.moveRigth(screen)

    pygame.quit()
    sys.exit()

if __name__ == "__main__" :
    main()
