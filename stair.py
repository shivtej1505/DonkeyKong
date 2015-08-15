import pygame
import random
from config import *

class Stair :
    def __init__(self,stairType) :
        self.__stairType = stairType

    def makeStair(self) :
        if self.__stairType == "Complete" :
            myStair = pygame.sprite.Sprite()
            myStair.image = pygame.image.load('stairs.png')
            myStair.rect = myStair.image.get_rect()
            return myStair
        elif self.__stairType == "Broken" :
            myStair = pygame.sprite.Sprite()
            myStair.image = pygame.image.load('broken_stairs.png')
            myStair.rect = myStair.image.get_rect()
            return myStair


def addStairs(screen) :
	stair_group = pygame.sprite.OrderedUpdates()
	for i in range(8) :
	    stair = Stair("Complete").makeStair()
	    stair.rect.left = random.randint(1,NUM_TILES_WIDTH-1) * TILE_SIZE
	    stair.rect.top =  204 + i*70
	    stair_group.add(stair)
        stair_group.draw(screen)

def addBrokenStairs(screen) :
	broken_stair_group = pygame.sprite.OrderedUpdates()
	for i in range(8):
	    broken_stair_top = Stair("Broken").makeStair()
	    pos = random.randint(1,NUM_TILES_WIDTH-1) * TILE_SIZE
	    broken_stair_top.rect.left = pos 
	    broken_stair_top.rect.top =  202 + i*70
	    broken_stair_group.add(broken_stair_top)
	    broken_stair_down = Stair("Broken").makeStair()
	    broken_stair_down.rect.left = pos
	    broken_stair_down.rect.top =  250 + i*70
	    broken_stair_group.add(broken_stair_down)
        broken_stair_group.draw(screen)
