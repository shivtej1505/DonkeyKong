import pygame

class Coin :
    def __init__(self) :
        self.__myCoin = pygame.sprite.Sprite()
        self.__myCoin.image = pygame.image.load('coin.png')
        self.__myCoin.rect = self.__myCoin.image.get_rect()
    
    def makeCoin(self) :
        return self.__myCoin


