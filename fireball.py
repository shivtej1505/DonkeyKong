import pygame
import random
from config import *
import level
pygame.init()

class Fireball :
    
    def makeFireball(self) :
        self.__myFire = pygame.sprite.Sprite()
        self.__myFire.image = pygame.image.load('fireball_new.png')
        self.__myFire.rect = self.__myFire.image.get_rect()
        self.__myFire.rect.left = 120
        self.__myFire.rect.top = 170
        self.__myFire.speedH = random.choice([-5,5])
        self.__myFire.barNo = 8
        return self.__myFire 
    
    def makeFireSource(self) :
        self.__myFireSource = pygame.sprite.Sprite()
        self.__myFireSource.image = pygame.image.load('fireball_source.png')
        self.__myFireSource.rect = self.__myFireSource.image.get_rect()
        self.__myFireSource.rect.left = 140
        self.__myFireSource.rect.top = 150
        return self.__myFireSource 
    
    def moveBalls(self) :
        self.setPosition("L", self.__myFire.speedH);        
        self.setBarNo()
    '''
    def setSpeedP(self) :
        self.__myFire.speedH = 10
    def setSpeedN(self) :
        self.__myFire.speedH = -10
    '''

    def getPosition(self, direction) :
        if direction == "U":
            return self.__myFire.rect.top
        elif direction == "D":
            return self.__myFire.rect.top + 30
        elif direction == "L":
            return self.__myFire.rect.left
        elif direction == "R":
            return self.__myFire.rect.left + 30

    def setPosition(self, direction, displacement) :
        if direction == "U":
            self.__myFire.rect.top -= displacement
        elif direction == "D":
            self.__myFire.rect.top += displacement
        elif direction == "L":
            self.__myFire.rect.left -= displacement
        elif direction == "R":
            self.__myFire.rect.left += displacement

    def setBarNo(self):
        barList = level.Level1bars()
        barList.reverse()
        print barList
        print self.getPosition("D")
        for i in range(len(barList)-1) :
            if self.getPosition("D") <= barList[i] and self.getPosition("D") > barList[i+1] :
                self.__myFire.barNo = i+1
    
    def getBarNo(self):
        return self.__myFire.barNo

    def gravity(self) :
        barsStart = level.Level1barsWidths()
        onBar = self.__myFire.barNo
        print "At Bar" + str(onBar)
        if onBar%2 == 1 :
            if self.getPosition("L") < barsStart[0] :
                y = self.getPosition("D")
                self.setPosition("D",-y+800)
            elif self.getPosition("R") > WIDTH - 120 :
                if onBar == 1:
                    self.setPosition("D",20)
                else:
                    self.setPosition("D",80)
        else :
            if self.getPosition("L") < barsStart[1] :
                self.setPosition("D",80)
            elif self.getPosition("L") > WIDTH - 110 :
                y = self.getPosition("D")
                self.setPosition("D",-y+800)
        self.setBarNo()

    def onBarless(self) :
        self.setPosition("D",80)
        self.setBarNo()
