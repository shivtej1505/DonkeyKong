import pygame
import random
from config import *
import level
pygame.init()

class Fireball :
    def __init__(self) :
        self.__myFire = pygame.sprite.Sprite()
        self.__myFire.image = pygame.image.load('fireball2_new.png')
        self.__myFire.rect = self.__myFire.image.get_rect()
        self.__myFire.rect.left = 120
        self.__myFire.rect.top = 170
        self.__myFire.speedH = random.choice([-5,5])
        self.__myFire.barNo = 8

    def makeFireball(self) :
        return self.__myFire 
    
    def killFireball(self) :
        if self.getPosition("D") > 770 :
            self.__myFire.kill()

    def makeFireSource(self) :
        self.__myFireSource = pygame.sprite.Sprite()
        self.__myFireSource.image = pygame.image.load('fireball2_source.png')
        self.__myFireSource.rect = self.__myFireSource.image.get_rect()
        self.__myFireSource.rect.left = 140
        self.__myFireSource.rect.top = 140
        return self.__myFireSource 
    
    def moveBalls(self) :
        self.setPosition("L", self.__myFire.speedH);        
        self.setBarNo()
    def setSpeedP(self) :
        self.__myFire.speedH = 5
    def setSpeedN(self) :
        self.__myFire.speedH = -5

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
            self.__myFire.speedH = random.choice([-5,5])
        elif direction == "L":
            self.__myFire.rect.left -= displacement
        elif direction == "R":
            self.__myFire.rect.left += displacement

    def setBarNo(self):
        barList = level.Level1bars()
        barList.reverse()
        for i in range(len(barList)-1) :
            if self.getPosition("D") <= barList[i] and self.getPosition("D") > barList[i+1] :
                self.__myFire.barNo = i+1
    
    def getBarNo(self):
        return self.__myFire.barNo

    def gravity(self) :
        barsStart = level.Level1barsWidths()
        onBar = self.__myFire.barNo
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
        stairListTop = level.Level1stairsTop()
        stairListTop.reverse()
        stairListTop.pop()
        stairListTop.insert(0,780)

        '''
        print self.getPosition("D")
        print self.getPosition("L")
        print self.__myFire.barNo
        '''
        luck = random.choice([True,False])

        # full stairs
        if  self.getBarNo() == 8 or self.getBarNo() == 5 or self.getBarNo() == 2 :
            if self.getPosition("L") == 540 and ( self.getPosition("D") in stairListTop[1::3]) and luck:
                self.setPosition("D",80)
                self.setBarNo()
        elif  self.getBarNo() == 7 or self.getBarNo() == 4 or self.getBarNo() == 1 :
            if self.getPosition("L") == 300 and ( self.getPosition("D") in stairListTop[0::3]) and luck:
                self.setPosition("D",80)
                self.setBarNo()
        elif  self.getBarNo() == 6 or self.getBarNo() == 3 :
            if self.getPosition("L") == 780 and ( self.getPosition("D") in stairListTop[2::3]) and luck:
                self.setPosition("D",80)
                self.setBarNo()
        
        # broken stairs
        if  self.getBarNo() == 8 or self.getBarNo() == 5 or self.getBarNo() == 2 :
            if self.getPosition("L") == 180 and ( self.getPosition("D") in stairListTop[1::3]) and luck:
                self.setPosition("D",80)
                self.setBarNo()
        elif  self.getBarNo() == 7 or self.getBarNo() == 4 or self.getBarNo() == 1 :
            if self.getPosition("L") == 390 and ( self.getPosition("D") in stairListTop[0::3]) and luck:
                self.setPosition("D",80)
                self.setBarNo()
        elif  self.getBarNo() == 6 or self.getBarNo() == 3 :
            if self.getPosition("L") == 600 and ( self.getPosition("D") in stairListTop[2::3]) and luck:
                self.setPosition("D",80)
                self.setBarNo()

