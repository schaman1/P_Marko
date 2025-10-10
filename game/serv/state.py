import pygame
from texture import color
from C_button import Button

class State:

    def __init__(self,screen,screenSize,font,Game):
        self.screen = screen
        self.Size = screenSize
        self.font = font
        self.Game = Game

        self.connexion = Button(pygame.Rect(self.Size[0]/3, 2*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6),color["GREEN"],"Connexion",self.font,"connexion")
        self.host = Button(pygame.Rect(self.Size[0]/3, 7*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6),color["GREY"],"Create serv",self.font,"host")
        self.quit = Button(pygame.Rect(self.Size[0]/3, 12*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6),color["RED"],"Quit",self.font,"quit")

        self.play = Button(pygame.Rect(self.Size[0]/3, 2*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6),color["GREEN"],"Play",self.font,"play")
        self.ip = Button(pygame.Rect(self.Size[0]/3, 7*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6),color["GREY"],"Ip:port",self.font,"ip")
        self.ip.create_input("RIGHT",color["BLACK"],"")

        self.show_ip = Button(pygame.Rect(self.Size[0]/3, 7*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6),color["GREY"],"ip:port = ",self.font,"show_ip")

        self.menu = Button(pygame.Rect(self.Size[0]*2.5/6, 15.5*self.Size[1]/18, self.Size[0]/6, self.Size[1]/12),color["RED"],"Menu",self.font,"menu")

        #dic boutton menu : 1= rect, 2=couleur, 3=texte
        self.dicMenu = {"connexion": self.connexion,
                        "host": self.host,
                        "quit": self.quit}
        
        self.dicConnexion = {"ip": self.ip,
                            "play": self.play,
                            "menu": self.menu}
        
        self.dicSettings = {"menu": self.menu,
                            "play": self.play,
                            "ip": self.show_ip}

    def a_state(self,state):

        self.screen.fill(color["BLACK"])

        if state == "menu":
            
            for btn in self.dicMenu.values():

                btn.draw(self.screen)

        elif state == "game":

            None
            #inGame_PostFase to do (choose skin, map, etc)
            #self.screen.fill(color["BLACK"])
            #.drawAll()

        elif state == "connexion":

            for btn in self.dicConnexion.values():

                btn.draw(self.screen)

        elif state == "host":

            for btn in self.dicSettings.values():

                btn.draw(self.screen)

        else : 
            pass