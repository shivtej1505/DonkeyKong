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

    def getDown(self) :
        stairListTop = level.Level1stairsTop()
        stairListTop.reverse()
        stairList = level.Level1stairs()
        '''
        atStop = self.getPosition("D")+1 in stairListTop
        '''
        godown = self.getPosition("L") in stairList
        if self.getPosition("D") == stairListTop[self.__myPlayer.barNo-2]  and godown :
            return True
        else:
            return False

    def printPos(self) :
        pass
        print "UP :" + str(self.getPosition("U"))
        print "DOWN :" + str(self.getPosition("D"))
        print "LEFT :" + str(self.getPosition("L"))
        print "RIGHT :" + str(self.getPosition("R"))
        
    def isMoveSide(self) :
        barList = level.Level1bars()
        if self.getPosition("D") in barList:
            return True
        else :
            return False

    def setBarNo(self):
        barList = level.Level1bars()
        barList.reverse()
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

    def moveDown(self, screen,hero_group,stairGroup) :
        barList = level.Level1bars()
        barList.reverse()
        collision = pygame.sprite.groupcollide(hero_group, level.getStairGroup(),False,True)
        print "player "+str(self.getPosition("D"))
        print "bar " +str(barList[self.__myPlayer.barNo-1])
        print "barNo " + str(self.__myPlayer.barNo)
        if len(collision) > 0:
            print "Collision"
            #if self.getPosition("D") + 20 <= barList[self.__myPlayer.barNo-1] or ( self.getPosition("D") + 20 <= barList[self.__myPlayer.barNo-1] and self.getDown()) :
            if self.getPosition("D") + 20 <= barList[self.__myPlayer.barNo-1] :
                self.setPosition("D",20)
        elif self.getDown() :
                self.setPosition("D",20)
        self.setBarNo()

    def moveLeft(self, screen) :
        if self.getPosition("L") > 10 and self.isMoveSide() :
            self.setPosition("L",TILE_SIZE)

    def moveRigth(self, screen) :
        if self.getPosition("R") < WIDTH - 20 and self.isMoveSide() :
            self.setPosition("R",TILE_SIZE)
