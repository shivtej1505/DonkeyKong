import pygame
from person import Person
from config import *
from stair import Stair
import level
import levelInit
pygame.init()

class Player(Person) :

    def makePlayer(self,lifes) :
        self.__myPlayer = pygame.sprite.Sprite()
        self.__myPlayer.image = pygame.image.load('person_new.png')
        self.__myPlayer.rect = self.__myPlayer.image.get_rect()
        self.__myPlayer.rect.left = 30
        self.__myPlayer.rect.top = 730
        self.__myPlayer.barNo = 1
        self.__myPlayer.jmpVel = 0
        self.__myPlayer.state = "STANDING"
        self.__myPlayer.life = lifes
        return self.__myPlayer
    
    def playerDied(self,screen) :
        self.__myPlayer.life -= 1
        levelInit.playerKilled(self.__myPlayer.life,screen)
        return self.__myPlayer.life
    
    def setState(self,state) :
        self.__myPlayer.state = state

    def getState(self) :
        return self.__myPlayer.state

    def jump(self,times) :
        barList = level.Level1bars()
        if self.getState() == "JUMPING" :
            if self.getPosition("D") in barList :
                self.setPosition("U",30)
            elif self.getPosition("D") -30 in barList : 
                self.setPosition("U",20)
            else :
                self.setPosition("U",-25)
            return times+1
        else :
            return times
    
    def allowLeft(self) :
        self.setPosition("L",20)

    def allowRight(self) :
        self.setPosition("R",20)

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
        godown = self.getPosition("L") in stairList
        if self.getPosition("D") == stairListTop[self.__myPlayer.barNo-2]  and godown :
            return True
        else:
            return False

    def printPos(self) :
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
    
    def gravity(self) :
        barList = level.Level1bars()
        barList.reverse()
        barsStart = level.Level1barsWidths()
        onBar = self.__myPlayer.barNo
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

    def setBarNo(self):
        barList = level.Level1bars()
        barList.reverse()
        for i in range(len(barList)-1) :
            if self.getPosition("D") <= barList[i] and self.getPosition("D") > barList[i+1] :
                self.__myPlayer.barNo = i+1

    def getBarNo(self):
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
        if len(collision) > 0:
            if self.getPosition("D") + 20 <= barList[self.__myPlayer.barNo-1] :
                self.setPosition("D",20)
        elif self.getDown() :
                self.setPosition("D",20)
        self.setBarNo()

    def moveLeft(self, screen) :
        if self.getPosition("L") > 10 and self.isMoveSide() :
            self.setPosition("L",TILE_SIZE)
        self.gravity()

    def moveRigth(self, screen) :
        if self.getPosition("R") < WIDTH - 20 and self.isMoveSide() :
            self.setPosition("R",TILE_SIZE)
        self.gravity()
