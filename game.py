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
    score = 0
    COINS = 20
    times = 0

    done = False
    donkey = Donkey()
    donkey_group = pygame.sprite.GroupSingle(donkey.makeDonkey())

    hero = Player()
    hero_group = pygame.sprite.GroupSingle(hero.makePlayer(lifes))

    fireball_group =  pygame.sprite.OrderedUpdates()
    Fireballs = []
    
    fireballS = Fireball()
    fireSource = pygame.sprite.GroupSingle(fireballS.makeFireSource())
    
    coinGroup = comLevels.genCoins(COINS)

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
                elif event.key == pygame.K_SPACE :
                    hero.setState("JUMPING")
                elif event.key == pygame.K_w or event.key == pygame.K_UP :
                    hero.moveUP(screen,hero_group,level.getStairGroup())
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN :
                    hero.moveDown(screen,hero_group,level.getStairGroup())
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT :
                    if hero.getState == ("JUMPING") :
                        hero.allowLeft()
                    hero.moveLeft(screen)
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT :
                    if hero.getState() == "JUMPING" :
                        hero.allowRight()
                    hero.moveRigth(screen)
                elif event.key == pygame.K_f :
                    for ball in Fireballs :
                        ball.setSpeedP()
                elif event.key == pygame.K_b :
                    for ball in Fireballs :
                        ball.setSpeedN()
            if event.type == pygame.USEREVENT :
                donkey.move()
                donkey.chgSpeed()
            if event.type == FIRETIME :
                fireball = Fireball()
                fireball_group.add(fireball.makeFireball())            
                Fireballs.append(fireball)
            for ball in Fireballs :
                ball.moveBalls()
                ball.gravity()
                ball.onBarless()
                ball.killFireball()

        collDon = pygame.sprite.groupcollide(donkey_group,hero_group,False,True)
        collFire = pygame.sprite.groupcollide(fireball_group,hero_group,False,True)
        if len(collDon) > 0 or len(collFire) > 0 :
            if score >= 25 :
                score -= 25
            else :
                score = 0
            print "player: D " + str(hero.getPosition("D"))
            print "player: L " + str(hero.getPosition("L"))
            print "donkey: D " + str(donkey.getPosition("D"))
            print "donkey: L " + str(donkey.getPosition("L"))
            lifes = hero.playerDied(screen)
            pygame.display.update()
            hero_group = pygame.sprite.GroupSingle(hero.makePlayer(lifes))
            try:
                time.sleep(3)
            except :
                print "key"
        
        collCoin = pygame.sprite.groupcollide(coinGroup,hero_group,True,False)
        if len(collCoin) > 0 :
            score += 20
        
        print "times" + str(times)
        times = hero.jump(times)
        if times == 3:
            hero.setState("STANDING")
            times = 0
        level.selectLevel(screen,1)
        coinGroup.draw(screen)
        hero_group.draw(screen)
        fireSource.draw(screen)
        fireball_group.draw(screen)
        donkey_group.draw(screen)
        comLevels.updateLife(lifes,screen)
        comLevels.updateScore(score,screen)
        pygame.display.update()
        
        if lifes == 0:
            break


    pygame.quit()
    sys.exit()

if __name__ == "__main__" :
    main()
