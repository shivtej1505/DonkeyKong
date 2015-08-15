import pygame
from config import *

# stuffs common in all levels
def commonInit(screen):
	# Outline lines
	pygame.draw.line(screen, (0,0,255) , (1, 1), (WIDTH-1, 1), 5)
	pygame.draw.line(screen, (0,0,255) , (WIDTH-1, 1), (WIDTH-1, HEIGHT-1), 5)
	pygame.draw.line(screen, (0,0,255) , (WIDTH-1, HEIGHT-1), (1, HEIGHT-1), 5)
	pygame.draw.line(screen, (0,0,255) , (1, HEIGHT-1), (1, 1), 5)

	# Cage maker
	pygame.draw.line(screen, (255,0,255) , (50, 130), (WIDTH/2, 130), 2)
	pygame.draw.line(screen, (255,0,255) , (50, 134), (WIDTH/2, 134), 2)
