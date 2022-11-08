import pygame
import sys
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                dt = self.clocl.tick()/1000
                pygame.display.update()



if __name__ == '__main__':
    game = Game()
    game.run()


