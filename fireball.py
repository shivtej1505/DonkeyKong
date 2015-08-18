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
        self.__myFire.rect.top = 175
        self.__myFire.speed = random.choice([-10,10])
        self.__myFire.barNo = 8
        return self.__myFire 
    
    def makeFireSource(self) :
        self.__myFireSource = pygame.sprite.Sprite()
        self.__myFireSource.image = pygame.image.load('fireball_source.png')
        self.__myFireSource.rect = self.__myFireSource.image.get_rect()
        self.__myFireSource.rect.left = 120
        self.__myFireSource.rect.top = 150
        return self.__myFireSource 
    
    def moveBalls(self) :
        self.__myFire.rect.left += self.__myFire.speed 
        self.setBarNo()

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
            if self.__myFire.rect.top - displacement > 70 :
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

        for i in range(len(barList)-1) :
            if self.getPosition("D") <= barList[i] and self.getPosition("D") > barList[i+1] :
                self.__myFire.barNo = i+1

    def getBarNo(self):
        return self.__myFire.barNo

    
    def gravity(self) :
        barsStart = level.Level1barsWidths()
        onBar = self.getBarNo()

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



