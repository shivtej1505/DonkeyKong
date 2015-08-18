import pygame
import random
from stair import *
from config import *
import levelInit

def selectLevel(screen ,Level):

    if Level == 1 :
        makeLevel1(screen)

myStair = Stair()

def getStairGroup():
    return myStair.getStairGroup()

def makeLevel1(screen):
    screen.fill((255, 255, 255))

    k = 1
    for i in range(200 ,800 ,80):
        if k%2 == 0:
            pygame.draw.line(screen, (255 ,0 ,255) , (30, i), (WIDTH - 120, i), 2)
        else:
            pygame.draw.line(screen, (255 ,0 ,255) , (120, i),(WIDTH - 90, i), 2)
        k += 1
	#pygame.draw.line(screen, (255,0,255) , (1, i+4), (WIDTH-1, i+4), 2)
    
    picked = True
    levelInit.commonInit(screen)
    myStair.addStairs(screen)
    myStair.addBrokenStairs(screen)

def Level1bars():
    return [40 ,120 ,200 ,280 ,360 ,440 ,520 ,600 ,680 ,760]

def Level1stairs():
    return [300 ,540 ,780]

def Level1stairsTop():
    return [120, 200, 280, 360, 440, 520, 600, 680]

