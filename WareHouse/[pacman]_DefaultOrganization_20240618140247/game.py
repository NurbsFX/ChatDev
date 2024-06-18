'''
This file contains the Game class.
'''
import pygame
import sys
from pygame.locals import *
from pacman import Pacman
from ghost import Ghost
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.pacman = Pacman(400, 300)
        self.ghosts = [Ghost(200, 200), Ghost(600, 200), Ghost(400, 400)]
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    def update(self):
        # Update game logic here
        pass
    def render(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.circle(self.screen, (255, 255, 0), (self.pacman.x, self.pacman.y), 10)
        for ghost in self.ghosts:
            pygame.draw.circle(self.screen, (255, 0, 0), (ghost.x, ghost.y), 10)
        pygame.display.flip()
    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)