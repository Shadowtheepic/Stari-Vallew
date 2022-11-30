import pygame
import sys
from settings import *
from level import Level




class Game:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.level = Level() #MO: this was the problem! you have to define your screen mode before you call anything that uses it (like convert alpha)
        self.clock = pygame.time.Clock()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            dt = self.clock.tick()/1000
            self.level.run(dt)
            pygame.display.update()



if __name__ == '__main__':
    game = Game()
    game.run()

