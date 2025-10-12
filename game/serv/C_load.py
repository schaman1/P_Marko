import pygame,math

class Load :

    def __init__(self,screen,nbr,radius = 10, distance = 50):
        self.nbr = nbr
        self.angle = 0
        self.screen = screen
        self.mid = (self.screen.get_rect().center)
        self.radius = radius
        self.distance = distance

    def draw(self):
        for i in range(self.nbr):
            pygame.draw.circle(self.screen,(50,50,50),self.calcul_pos(i),self.radius)

    def calcul_pos(self,idx):

        angle = self.angle + 360/self.nbr*idx

        x = math.cos(angle) * self.distance
        y = math.sin(angle) * self.distance

        return (x+ self.mid[0],y + self.mid[1])