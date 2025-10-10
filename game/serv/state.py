import pygame, threading
from texture import color
from C_button import Button

class State:

    def __init__(self,screen,screenSize,font,Game):
        self.screen = screen
        self.Size = screenSize
        self.font = font
        self.Game = Game

        self.connexion = Button(pygame.Rect(self.Size[0]/3, 2*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6),color["GREEN"],"Rejoindre une partie",self.font,"connexion")
        self.host = Button(pygame.Rect(self.Size[0]/3, 7*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6),color["GREY"],"Creer une partie",self.font,"host")
        self.quit = Button(pygame.Rect(self.Size[0]/3, 12*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6),color["RED"],"Quit",self.font,"quit")

        self.start = Button(pygame.Rect(self.Size[0]/3, 2*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6),color["GREEN"],"Lancer la partie",self.font,"start")
        self.ip = Button(pygame.Rect(self.Size[0]/3, 7*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6),color["GREY"],"Ip:port",self.font,"ip")
        self.ip.create_input("RIGHT",color["BLACK"],"")

        self.show_ip = Button(pygame.Rect(self.Size[0]/3, 7*self.Size[1]/18, self.Size[0]/3, self.Size[1]/6),color["GREY"],"ip:port = ",self.font,"show_ip")

        self.menu = Button(pygame.Rect(self.Size[0]*2.5/6, 15.5*self.Size[1]/18, self.Size[0]/6, self.Size[1]/12),color["RED"],"Menu",self.font,"menu")

        #dic boutton menu : 1= rect, 2=couleur, 3=texte
        self.dicMenu = {"connexion": self.connexion,
                        "host": self.host,
                        "quit": self.quit}
        
        self.dicConnexion = {"ip": self.ip,
                            "start": self.start,
                            "menu": self.menu}
        
        self.dicSettings = {"menu": self.menu,
                            "start": self.start,
                            "ip": self.show_ip}

    def a_state(self,state):

        self.screen.fill(color["BLACK"])

        if state == "menu":
            
            for btn in self.dicMenu.values():

                btn.draw(self.screen)

        elif state == "game":

            None
            #inGame_PostFase to do (choose skin, map, etc)
            self.screen.fill(color["BLACK"])
            #.drawAll()

        elif state == "wait_serv":

            self.screen.fill(color["BLACK"])
            waiting_text = self.font.render("En attente du créateur pour lancer la partie...", True, color["WHITE"])
            text_rect = waiting_text.get_rect(center=(self.Size[0]//2, self.Size[1]//2))
            self.screen.blit(waiting_text, text_rect)

        elif state == "connexion":

            for btn in self.dicConnexion.values():

                btn.draw(self.screen)

        elif state == "host":

            for btn in self.dicSettings.values():

                btn.draw(self.screen)

        else : 
            pass

    def connexion_serv(self,client):
        """renvoie le mode de jeu apres connexion"""
        ip_port = self.ip.dicRect[self.ip.id+"_input"]["text"][:-1]

        self.start.update_text("start","Connexion...")
        threading.Thread(target=client.connexion_serveur, args=(ip_port,)).start()

        start_time = pygame.time.get_ticks()
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Temps écoulé en secondes

        while client.connected == None and elapsed_time < 5:  # Attendre la connexion ou un timeout de 5 secondes

            elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

            if client.connected == False:
                self.start.update_text("start",client.err_messsage)
                return "connexion"
            
            elif client.connected : 
                print("En attente du serveur...")
                return "wait_serv"

        self.start.update_text("start","Echec de la connexion")
        return "connexion"