# Main game file
import pygame
import random
import sys
from player import Player
from donkey import Donkey
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
    donkey = Donkey()
    donkey_group = pygame.sprite.GroupSingle(donkey.makeDonkey())

    hero = Player()
    hero_group = pygame.sprite.GroupSingle(hero.makePlayer())

    fireball = Fireball()
    fireball_group =  pygame.sprite.OrderedUpdates()
    Fireballs = []
    
    fireSource = pygame.sprite.GroupSingle(fireball.makeFireSource())

    pygame.key.set_repeat(8,10)
    FIRETIME = pygame.USEREVENT + 1
    pygame.time.set_timer(pygame.USEREVENT, 150)
    pygame.time.set_timer(FIRETIME, 1500)

    while done == False :

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                done = True
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    done = True
                elif event.key == pygame.K_w or event.key == pygame.K_UP :
                    hero.moveUP(screen,hero_group,level.getStairGroup())
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN :
                    hero.moveDown(screen,hero_group,level.getStairGroup())
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT :
                    hero.moveLeft(screen)
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT :
                    hero.moveRigth(screen)
            if event.type == pygame.USEREVENT :
                donkey.move()
                donkey.chgSpeed()
            if event.type == FIRETIME :
                fireball_group.add(fireball.makeFireball())            
                Fireballs.append(fireball)
            for ball in Fireballs :
                ball.moveBalls()
                ball.gravity()
        
        level.selectLevel(screen,1)
        hero_group.draw(screen)
        fireSource.draw(screen)
        fireball_group.draw(screen)
        donkey_group.draw(screen)
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__" :
    main()
