#!/usr/bin/python3
import sys
import pygame

from classes.ObstacleFactory import ObstacleFactory
from classes.Tank import Tank

pygame.init()


class Game:

    def __init__(self, screen):

        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.screen_size = self.scr_width, self.scr_height

        # Background Game
        self.bg = pygame.image.load("resources/arena.jpeg")
        self.bg_rect = self.bg.get_rect()

        # Sound Game
        # self.laser_sound = pygame.mixer.Sound('resources/sounds/laser_shot.wav')
        # self.laser_sound.set_volume(0.2)

        self.clock = pygame.time.Clock()

        self.time_elapsed_since_last_action = 0
        self.clock = pygame.time.Clock()

    def run(self):
        mainloop = True
        while mainloop:
            self.clock.tick(50)
            self.screen.fill([0, 0, 0])
            self.screen.blit(self.bg, self.bg_rect)

            # Close the game when the red cross is clicked
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Keyboard Events
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                pass
            elif keys[pygame.K_RIGHT]:
                pass
            elif keys[pygame.K_UP]:
                pass
            elif keys[pygame.K_DOWN]:
                pass
            elif keys[pygame.K_SPACE]:
                pass
            elif keys[pygame.K_ESCAPE]:
                # Go back to the game menu
                mainloop = False

            dt = self.clock.tick()

            self.time_elapsed_since_last_action += dt
            # dt is measured in milliseconds, therefore 250 ms = 0.25 seconds

            # generate a new car with this timer
            if self.time_elapsed_since_last_action > 20:
                self.time_elapsed_since_last_action = 0

            self.screen.blit()

            pygame.display.flip()
