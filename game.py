# Main game file
import pygame
import random
import sys
import level
import time
import levelInit as comLevels
from player import Player
from donkey import Donkey
from config import *
from stair import *
from fireball import Fireball

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("DonkeyKong")
    
    # Initialize level
    
    lifes = 3

    done = False
    donkey = Donkey()
    donkey_group = pygame.sprite.GroupSingle(donkey.makeDonkey())

    hero = Player()
    hero_group = pygame.sprite.GroupSingle(hero.makePlayer(lifes))

    fireball = Fireball()
    fireball_group =  pygame.sprite.OrderedUpdates()
    Fireballs = []
    fireball_group.add(fireball.makeFireball())            
    Fireballs.append(fireball)
    
    fireSource = pygame.sprite.GroupSingle(fireball.makeFireSource())

    pygame.key.set_repeat(8,10)
    FIRETIME = pygame.USEREVENT + 1
    pygame.time.set_timer(pygame.USEREVENT, 150)
    pygame.time.set_timer(FIRETIME, 2000)

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
                '''
                elif event.key == pygame.K_f :
                    for ball in Fireballs :
                        ball.setSpeedP()
                elif event.key == pygame.K_b :
                    for ball in Fireballs :
                        ball.setSpeedN()
                ''' 
            if event.type == pygame.USEREVENT :
                donkey.move()
                donkey.chgSpeed()
            '''
            if event.type == FIRETIME :
                fireball_group.add(fireball.makeFireball())            
                Fireballs.append(fireball)
            '''
        for ball in Fireballs :
            ball.moveBalls()
            ball.gravity()
            ball.onBarless()

        collision = pygame.sprite.groupcollide(donkey_group,hero_group,False,True)
        if len(collision) > 0:
            lifes = hero.playerDied(screen)
            pygame.display.update()
            hero_group = pygame.sprite.GroupSingle(hero.makePlayer(lifes))
            try:
                time.sleep(3)
            except :
                print "key"

        level.selectLevel(screen,1)
        hero_group.draw(screen)
        fireSource.draw(screen)
        fireball_group.draw(screen)
        donkey_group.draw(screen)
        comLevels.updateLife(lifes,screen)
        pygame.display.update()
        
        if lifes == 0:
            break


    pygame.quit()
    sys.exit()

if __name__ == "__main__" :
    main()
