import pygame
from person import Person
from config import *
from stair import Stair
import level
pygame.init()

class Player(Person) :
    #def __init__(self) :
    #    super(self.__class__,self).__init__()
    #    self.__playerGroup = pygame.sprite.GroupSingle()
    
    # returns playerGroup
    #def getPlayerGroup() :
    #    return self.__playerGroup

    def makePlayer(self) :
        self.__myPlayer = pygame.sprite.Sprite()
        self.__myPlayer.image = pygame.image.load('person_new.png')
        self.__myPlayer.rect = self.__myPlayer.image.get_rect()
        self.__myPlayer.rect.left = 30
        self.__myPlayer.rect.top = 725
        return self.__myPlayer

    def getPosition(self, direction) :
        if direction == "U":
            return self.__myPlayer.rect.top
        elif direction == "D":
            return self.__myPlayer.rect.top - 35
        elif direction == "L":
            return self.__myPlayer.rect.left
        elif direction == "R":
            return self.__myPlayer.rect.left + 30

    def setPosition(self, direction, displacement) :
        if direction == "U":
            if self.__myPlayer.rect.top - displacement > 70 :
                self.__myPlayer.rect.top -= displacement
        elif direction == "D":
            self.__myPlayer.rect.top += displacement
        elif direction == "L":
            self.__myPlayer.rect.left -= displacement
        elif direction == "R":
            self.__myPlayer.rect.left += displacement
    

    def moveUP(self, screen,hero_group,stairGroup) :
        collision = pygame.sprite.groupcollide(hero_group, level.getStairGroup(),False,True)
        if len(collision) > 0:
            self.setPosition("U",20)

    def moveDown(self, screen,hero_group,stairGroup) :
        collision = pygame.sprite.groupcollide(hero_group, level.getStairGroup(),False,True)
        if len(collision) > 0:
            if self.getPosition("D") < 705 :
                print self.getPosition("U")
                self.setPosition("D",20)

    def moveLeft(self, screen) :
        if self.getPosition("L") > 10 :
            self.setPosition("L",TILE_SIZE)

    def moveRigth(self, screen) :
        if self.getPosition("R") < WIDTH - 20 :
            self.setPosition("R",TILE_SIZE)
