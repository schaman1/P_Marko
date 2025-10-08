import pygame
from state import State
from client import Client
#from C_inGame import InGame
#from C_card import Card

class Game:
    def __init__(self):
        # Set up the display (width, height)
        self.screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h),pygame.FULLSCREEN | pygame.SCALED)
        self.screenSize = (self.screen.get_width(),self.screen.get_height())

        #ecriture
        self.font = pygame.font.SysFont(None, 48)

        #Set up the clock for managing the frame rate
        self.fps = 60
        self.fpsClock = pygame.time.Clock()
        self.dt = 0 # Delta time between frames = devra faire *dt pour les mouvements

        #self.Game = InGame(self.screen,self.screenSize,self.font,self.cards)
        self.Game = None

        self.state = State(self.screen,self.screenSize,self.font,self.Game)
        self.mod = "menu" #menu/reglage/game
        self.client = Client()

    def run(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.mod == "menu":

                        if self.state.play.collidepoint(event.pos):
                            #("Play button clicked")
                            #self.Game.createHand()#initialise the hand of the player
                            
                            self.mod = "game"
                            print("game !")
                            self.client.connexion_serveur("localhost",5000)
                            


                        elif self.state.settings.collidepoint(event.pos):
                            print("Parametre button clicked")
                        elif self.state.quit.collidepoint(event.pos):
                            #("Quit button clicked")
                            running = False

    
            #Affiche ce qu'il doit être affiché en fonction du mode (reglage/menu/game)
            self.state.a_state(self.mod)

            # Update the display
            pygame.display.flip()

            self.dt = self.fpsClock.tick(self.fps) / 1000

        pygame.quit()
