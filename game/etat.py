import pygame
from texture import color

class State:

    def __init__(self,screen,screenSize,font,Game):
        self.screen = screen
        self.Size = screenSize
        self.font = font
        self.Game = Game

        self.play = pygame.Rect(self.Size[0]/3, 2*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6)
        self.settings = pygame.Rect(self.Size[0]/3, 7*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6)
        self.quit = pygame.Rect(self.Size[0]/3, 12*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6)

        #dic boutton menu : 1= rect, 2=couleur, 3=texte
        self.dicMenu = {"play": (self.play,color["GREEN"],"Play"),
                        "settings": (self.settings,color["GREY"],"Settings"),
                        "quit": (self.quit,color["RED"],"Quit")}

    def a_state(self,state):

        if state == "menu":
            
            for rect in self.dicMenu.values():
                pygame.draw.rect(self.screen,rect[1],rect[0],border_radius=10)

            # Centrer le texte dans le rectangle
                text = self.font.render(rect[2], True, color["BLACK"])  # True = anti-aliasing
                text_rect = text.get_rect(center=rect[0].center)
                self.screen.blit(text, text_rect)
        
        elif state == "game":

            #inGame_PostFase to do (choose skin, map, etc)
            self.screen.fill(color["BLACK"])
            self.Game.drawAll()

        else : 
            pass