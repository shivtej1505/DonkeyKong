import pygame
from person import Person
from config import *
pygame.init()

class Player(Person) :
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
            return self.__myPlayer.rect.top
        elif direction == "R":
            return self.__myPlayer.rect.top + 35

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

    def moveUP(self, screen) :
        self.setPosition("U",20)
        screen.blit(self.__myPlayer.image,(self.__myPlayer.rect.left, self.__myPlayer.rect.top))

    def moveDown(self, screen) :
        self.setPosition("D",20)
        screen.blit(self.__myPlayer.image,(self.__myPlayer.rect.left, self.__myPlayer.rect.top))

    def moveLeft(self, screen) :
        self.setPosition("L",TILE_SIZE)
        screen.blit(self.__myPlayer.image,(self.__myPlayer.rect.left, self.__myPlayer.rect.top))

    def moveRigth(self, screen) :
        self.setPosition("R",TILE_SIZE)
        screen.blit(self.__myPlayer.image,(self.__myPlayer.rect.left, self.__myPlayer.rect.top))
