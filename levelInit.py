import pygame
from config import *
from time import sleep
pygame.init()

# stuffs common in all levels
def commonInit(screen) :
    # Outline lines
    pygame.draw.line(screen, (0,0,255) , (1, 1), (WIDTH-1, 1), 5)
    pygame.draw.line(screen, (0,0,255) , (WIDTH-1, 1), (WIDTH-1, HEIGHT-1), 5)
    pygame.draw.line(screen, (0,0,255) , (WIDTH-1, HEIGHT-1), (1, HEIGHT-1), 5)
    pygame.draw.line(screen, (0,0,255) , (1, HEIGHT-1), (1, 1), 5)

    # Cage maker
    pygame.draw.line(screen, (255,0,255) , (20, 120), (WIDTH - 20, 120), 2)
    #pygame.draw.line(screen, (255,0,255) , (20, 124), (WIDTH - 20, 124), 2)

def updateLife(lifes, screen) :
    pygame.font.init()
    myFont = pygame.font.Font(None, 40)
    Lifes = myFont.render("Lifes :" + str(lifes), 1, (0, 0, 0))
    screen.blit(Lifes, (850, 15))

def playerKilled(lifes, screen) :
    killed = pygame.font.Font(None,100)
    doWrite = killed.render("killed", 1, (0, 0, 0))
    screen.blit(doWrite, (400,400))
    pygame.font.quit()
