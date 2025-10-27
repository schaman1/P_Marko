import pygame

class Game :
    def __init__(self, size,canva_size):
        self.cell_size = size
        self.canva_size = canva_size
        self.canva = pygame.Surface(canva_size)
        #self.canva_map = self.map.canva
        self.bg = pygame.image.load("assets/bg1.png").convert()


        # pré-calcul des rects pour chaque cellule
        self.rect_grid = [
            [pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
             for x in range(self.canva_size[0]//self.cell_size)]
            for y in range(self.canva_size[1]//self.cell_size)
        ]
    
    def update_canva(self,l):

        for e in l :
            self.switch_cell(e)

    def switch_cell(self,el):

        x,y,color = el
        pygame.draw.rect(self.canva, color, self.rect_grid[y][x])