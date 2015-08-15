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

        even = 0
	for i in range(-1,7) :
	    stair = Stair("Complete").makeStair()
            if even%3 == 0:
	        stair.rect.left =  26 * TILE_SIZE
            elif even%3 == 1:
	        stair.rect.left = 18 * TILE_SIZE
            else:
	        stair.rect.left = 10 * TILE_SIZE 
	    stair.rect.top =  204 + i*80
	    stair_group.add(stair)
            even += 1 
        stair_group.draw(screen)

def addBrokenStairs(screen) :
	broken_stair_group = pygame.sprite.OrderedUpdates()
        odd = 0
	for i in range(-1,7):
	    broken_stair_top = Stair("Broken").makeStair()
	    broken_stair_top.rect.top =  204 + i*80
	    broken_stair_down = Stair("Broken").makeStair()
	    broken_stair_down.rect.top =  254 + i*80
            if odd%3 == 0: 
        	pos = 6 * TILE_SIZE
	        broken_stair_top.rect.left = pos 
	        broken_stair_down.rect.left = pos
            elif odd%3 == 1:
        	pos = 13 * TILE_SIZE
	        broken_stair_top.rect.left = pos 
	        broken_stair_down.rect.left = pos
            else:
        	pos = 20 * TILE_SIZE
	        broken_stair_top.rect.left = pos 
	        broken_stair_down.rect.left = pos

	    broken_stair_group.add(broken_stair_down)
	    broken_stair_group.add(broken_stair_top)
            odd += 1
        broken_stair_group.draw(screen)
