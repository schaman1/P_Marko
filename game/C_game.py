import pygame
from etat import a_state

class Game:
    def __init__(self):
        # Set up the display (width, height)
        self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)

        #Set up the clock for managing the frame rate
        self.fps = 60
        self.fpsClock = pygame.time.Clock()
        self.dt = 0 # Delta time between frames = devra faire *dt pour les mouvements

    def run(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
    
            a_state("menu",self.screen)

            # Update the display
            pygame.display.flip()

            self.dt = self.fpsClock.tick(self.fps) / 1000

        pygame.quit()
