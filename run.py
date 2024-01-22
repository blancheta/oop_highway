#!/usr/bin/python3
import pygame
from screens.game import Game

pygame.init()

# set_mode(resolution=(width, height), flags=0, depth=0)
# flags : collection of qdditional options
# depth : number of bits use for colors
screen = pygame.display.set_mode((400, 600), 0, 32)
bg_color = (0, 0, 0)

# Views initialization
g = None

menu_selected = True
mainloop = True
while mainloop:

	screen.fill(bg_color)

	pygame.display.set_caption('Mini Car')
	g = Game(screen)
	g.run()

	pygame.display.flip()
