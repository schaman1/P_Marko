import pygame,io,base64
from serv.in_game.read_map import Read_map

class Server_game :
    def __init__(self):
        self.canva_size = (800,600)
        self.map = Read_map("assets/bgWater.png",10,self.canva_size)
        self.canva_map = self.map.canva
        self.bg = pygame.image.load("assets/bg1.png").convert()
        self.canva_send = pygame.Surface((800, 600))
        self.canva_send.fill((0,0,0))

    def give_canva(self):
        if self.map_changed(): #Pour opti après
            return (True,self.return_png_canva())
        return (False,None)
    
    def return_png_canva(self):
        surface = self.create_canva()
        data = pygame.image.tostring(surface, "RGB")  # pixels bruts
        return base64.b64encode(data).decode("utf-8")

    def map_changed(self):
        return True
    
    def create_canva(self):
        self.canva_map = self.map.return_map()

        self.canva_send.blit(self.bg,(0,0))
        self.canva_send.blit(self.canva_map,(0,0))

        return self.canva_send
