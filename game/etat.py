import pygame

class State:

    def __init__(self,screen,screenSize):
        self.screen = screen
        self.Size = screenSize


    def a_state(self,state):

        if state == "menu":


            play = pygame.draw.rect(self.screen, (0, 255, 0), (self.Size[0]/3, 2*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6))
            parametre = pygame.draw.rect(self.screen, (50, 0, 58), (self.Size[0]/3, 7*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6))
            quit = pygame.draw.rect(self.screen, (255, 0, 0), (self.Size[0]/3, 12*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6))
            

        else : 
            pass