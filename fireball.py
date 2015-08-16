import pygame
import random
from config import *
pygame.init()

class Fireball :
    def makeFireball(self) :
        self.__myFire = pygame.sprite.Sprite()
        self.__myFire.image = pygame.image.load('fireball.png')
        self.__myFire.rect = self.__myFire.image.get_rect()
        self.__myFire.rect.left = random.randint(10,25) * TILE_SIZE 
        self.__myFire.rect.top = random.randint(10,25) * TILE_SIZE 
        return self.__myFire 
