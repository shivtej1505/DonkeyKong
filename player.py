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
        self.__myPlayer.rect.top = 730
        self.__myPlayer.barNo = 1
        return self.__myPlayer
    
    def getPosition(self, direction) :
        if direction == "U":
            return self.__myPlayer.rect.top
        elif direction == "D":
            return self.__myPlayer.rect.top + 30
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
    
    def setBarNo(self):
        barList = level.Level1bars()
        barList.reverse()
        print barList
        print self.getPosition("D")
        for i in range(len(barList)-1) :
            if self.getPosition("D") <= barList[i] and self.getPosition("D") > barList[i+1] :
                self.__myPlayer.barNo = i+1

    def getBarNo(self):
        print self.__myPlayer.barNo
        return self.__myPlayer.barNo

    def moveUP(self, screen,hero_group,stairGroup) :
        collision = pygame.sprite.groupcollide(hero_group, level.getStairGroup(),False,True)
        if len(collision) > 0:
            self.setPosition("U",20)
        self.setBarNo()
        self.getBarNo()

    def moveDown(self, screen,hero_group,stairGroup) :
        collision = pygame.sprite.groupcollide(hero_group, level.getStairGroup(),False,True)
        if len(collision) > 0:
            if self.getPosition("D") < 760 :
                self.setPosition("D",20)
                print self.getPosition("D")
        self.setBarNo()
        self.getBarNo()

    def moveLeft(self, screen) :
        if self.getPosition("L") > 10 :
            self.setPosition("L",TILE_SIZE)

    def moveRigth(self, screen) :
        if self.getPosition("R") < WIDTH - 20 :
            self.setPosition("R",TILE_SIZE)
