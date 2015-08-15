import pygame
from person import Person
from config import *
pygame.init()

class Player(Person) :
    def makePlayer(self) :
        self.__myPlayer = pygame.sprite.Sprite()
        self.__myPlayer.image = pygame.image.load('person.jpg')
        self.__myPlayer.rect = self.__myPlayer.image.get_rect()
        self.__myPlayer.rect.left = 50
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
            self.__myPlayer.rect.top -= displacement
        elif direction == "D":
            self.__myPlayer.rect.top += displacement
        elif direction == "L":
            self.__myPlayer.rect.left -= displacement
        elif direction == "R":
            self.__myPlayer.rect.left += displacement

    def moveUP(self, screen) :
        self.setPosition("U",70/3)
        screen.blit(self.__myPlayer.image,(self.__myPlayer.rect.left, self.__myPlayer.rect.top))

    def moveDown(self, screen) :
        self.setPosition("D",70/3)
        screen.blit(self.__myPlayer.image,(self.__myPlayer.rect.left, self.__myPlayer.rect.top))

    def moveLeft(self, screen) :
        self.setPosition("L",TILE_SIZE)
        screen.blit(self.__myPlayer.image,(self.__myPlayer.rect.left, self.__myPlayer.rect.top))

    def moveRigth(self, screen) :
        self.setPosition("R",TILE_SIZE)
        screen.blit(self.__myPlayer.image,(self.__myPlayer.rect.left, self.__myPlayer.rect.top))
