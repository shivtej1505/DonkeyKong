import pygame
from person import Person

pygame.init()

class Donkey(Person) :

    def makeDonkey(self) :
	self.__myDonkey = pygame.sprite.Sprite()
        self.__myDonkey.image = pygame.image.load('donkey_new.png')
        self.__myDonkey.rect = self.__myDonkey.image.get_rect()
        self.__myDonkey.rect.left = 120
        self.__myDonkey.rect.top = 122
        self.__myDonkey.speed = 30
        return self.__myDonkey
    
    def move(self) :
        self.setPosition("L",self.__myDonkey.speed)
    
    def chgSpeed(self):
        if self.getPosition("L") >=  820:
            self.__myDonkey.speed = - self.__myDonkey.speed
        elif self.getPosition("L") < 115 :
            self.__myDonkey.speed = - self.__myDonkey.speed
            


    def getPosition(self, direction) :
        if direction == "U":
            return self.__myDonkey.rect.top
        elif direction == "D":
            return self.__myDonkey.rect.top + 30
        elif direction == "L":
            return self.__myDonkey.rect.left
        elif direction == "R":
            return self.__myDonkey.rect.left + 30

    def setPosition(self, direction, displacement) :
        if direction == "U":
            if self.__myDonkey.rect.top - displacement > 70 :
                self.__myDonkey.rect.top -= displacement
        elif direction == "D":
            self.__myDonkey.rect.top += displacement
        elif direction == "L":
            self.__myDonkey.rect.left += displacement
        elif direction == "R":
            self.__myDonkey.rect.left += displacement
    

