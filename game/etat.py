import pygame
from texture import color

class State:

    def __init__(self,screen,screenSize,font):
        self.screen = screen
        self.Size = screenSize
        self.font = font

        self.play = pygame.Rect(self.Size[0]/3, 2*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6)
        self.parametre = pygame.Rect(self.Size[0]/3, 7*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6)
        self.quit = pygame.Rect(self.Size[0]/3, 12*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6)

        

    def a_state(self,state):

        if state == "menu":

            
            
            pygame.draw.rect(self.screen, (0, 255, 0), self.play, border_radius=10)
            pygame.draw.rect(self.screen, (50, 0, 58), self.parametre, border_radius=10)
            pygame.draw.rect(self.screen, (255, 0, 0), self.quit, border_radius=10)

            # Centrer le texte dans le rectangle
            text = self.font.render("Quitter", True, color["BLACK"])  # True = anti-aliasing
            text_rect = text.get_rect(center=self.quit.center)
            self.screen.blit(text, text_rect)

        else : 
            pass