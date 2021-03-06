import pygame
import random
from config import *
from time import sleep
from coin import Coin
pygame.init()

# stuffs common in all levels
def commonInit(screen) :
    # Outline lines
    pygame.draw.line(screen, (0,0,255) , (1, 1), (WIDTH-1, 1), 5)
    pygame.draw.line(screen, (0,0,255) , (WIDTH-1, 1), (WIDTH-1, HEIGHT-1), 5)
    pygame.draw.line(screen, (0,0,255) , (WIDTH-1, HEIGHT-1), (1, HEIGHT-1), 5)
    pygame.draw.line(screen, (0,0,255) , (1, HEIGHT-1), (1, 1), 5)

    # Cage maker
    pygame.draw.line(screen, (255,0,255) , (20, 120), (WIDTH - 20, 120), 2)
    #pygame.draw.line(screen, (255,0,255) , (20, 124), (WIDTH - 20, 124), 2)

def updateLife(lifes, screen) :
    pygame.font.init()
    myFont = pygame.font.Font(None, 30)
    Lifes = myFont.render("Lifes :" + str(lifes), 1, (0, 0, 0))
    screen.blit(Lifes, (850, 15))

def updateScore(score, screen) :
    pygame.font.init()
    myFont = pygame.font.Font(None, 30)
    Score = myFont.render("Score :" + str(score), 1, (0, 0, 0))
    screen.blit(Score, (850, 40))

def playerKilled(lifes, screen) :
    killed = pygame.font.Font(None,100)
    doWrite = killed.render("killed", 1, (0, 0, 0))
    screen.blit(doWrite, (400,400))
    pygame.font.quit()

def genCoins(num) :
    coinGroup = pygame.sprite.OrderedUpdates()
    for coin in range(num) :
        myCoin = Coin().makeCoin()
        myCoin.rect.left = random.randint(1,20) * TILE_SIZE
        myCoin.rect.top = random.randint(1,10) * 80
        coinGroup.add(myCoin)
    return coinGroup
