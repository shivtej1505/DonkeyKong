import pygame
import random
from config import *

class Stair :
    def __init__(self) :
        self.__stair_group = pygame.sprite.OrderedUpdates()
        self.__broken_stair_group = pygame.sprite.OrderedUpdates()

    # makes the stairs. just need to draw them
    def makeStair(self,stairType) :
        if stairType == "Complete" :
            myStair = pygame.sprite.Sprite()
            myStair.image = pygame.image.load('stairs_new.png')
            myStair.rect = myStair.image.get_rect()
            return myStair
        elif stairType == "Broken" :
            myStair = pygame.sprite.Sprite()
            myStair.image = pygame.image.load('broken_stairs.png')
            myStair.rect = myStair.image.get_rect()
            return myStair

    # returns stair_group
    def getStairGroup(self) :
        return self.__stair_group

    # returns broken_stair
    def getBrokenStairGroup(self) :
        return self.__broken_stair_group

    # draws full stairs 
    def addStairs(self,screen) :
        even = 0
	for i in range(-1,7) :
	    stair = self.makeStair("Complete")
            if even%3 == 0:
	        stair.rect.left =  26 * TILE_SIZE
            elif even%3 == 1:
	        stair.rect.left = 18 * TILE_SIZE
            else:
	        stair.rect.left = 10 * TILE_SIZE 
	    stair.rect.top =  200 + i*80
	    self.__stair_group.add(stair)
            even += 1 
        self.__stair_group.draw(screen)
    
    # draws broken stairs
    def addBrokenStairs(self,screen) :
        odd = 0
	for i in range(0,7):
	    broken_stair_top = Stair().makeStair("Broken")
	    broken_stair_top.rect.top =  200 + i*80
	    broken_stair_down = Stair().makeStair("Broken")
	    broken_stair_down.rect.top =  250 + i*80
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

	    self.__broken_stair_group.add(broken_stair_down)
	    self.__broken_stair_group.add(broken_stair_top)
            odd += 1
        self.__broken_stair_group.draw(screen)
