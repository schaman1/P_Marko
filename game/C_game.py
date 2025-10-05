import pygame
from etat import State

class Game:
    def __init__(self):
        # Set up the display (width, height)
        self.screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h),pygame.FULLSCREEN | pygame.SCALED)
        self.screenSize = (self.screen.get_width(),self.screen.get_height())

        #Set up the clock for managing the frame rate
        self.fps = 60
        self.fpsClock = pygame.time.Clock()
        self.dt = 0 # Delta time between frames = devra faire *dt pour les mouvements

        self.state = State(self.screen,self.screenSize)
        self.mod = "menu" #menu/reglage/game

    def run(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.mod == "menu":
                        if self.state.play.collidepoint(event.pos):
                            print("Play button clicked")
                        elif self.state.parametre.collidepoint(event.pos):
                            print("Parametre button clicked")
                        elif self.state.quit.collidepoint(event.pos):
                            print("Quit button clicked")
                            running = False

    
            #Affiche ce qu'il doit être affiché en fonction du mode (reglage/menu/game)
            self.state.a_state(self.mod)

            # Update the display
            pygame.display.flip()

            self.dt = self.fpsClock.tick(self.fps) / 1000

        pygame.quit()
