import pygame
import math
import random

class Read_map:
    def __init__(self, filename, screen,size):
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.cell_size = size
        self.cells_w = self.width // self.cell_size
        self.cells_h = self.height // self.cell_size

        self.density = (2,1)  # 1 = pleine résolution, 2 = 1 pixel sur 2, etc.

        self.map = pygame.image.load(filename).convert()
        self.map = pygame.transform.scale(self.map, (self.width, self.height))
        self.canva = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.screen = screen

        # grille binaire + couleurs
        self.grid = [[None for _ in range(self.cells_w)] for _ in range(self.cells_h)]
        
        # sets plutôt que listes = O(1) lookup, remove, add
        self.cell_to_update = set()
        self.circle_patterns = {}
        self.border_patterns = {}

        # pré-calcul des rects pour chaque cellule
        self.rect_grid = [
            [pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
             for x in range(self.cells_w)]
            for y in range(self.cells_h)
        ]

        self.read_map()
        self.create_map()

    def get_color(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.map.get_at((x, y))[:3]
        return (0, 0, 0)

    def read_map(self):
        """Lit l'image et remplit la grille de cellules"""
        for cy in range(self.cells_h):
            for cx in range(self.cells_w):
                color = self.get_color(cx * self.cell_size, cy * self.cell_size)
                if color != (255, 255, 255):
                    if color == (97,66,0):
                        color = (random.randint(150,200),random.randint(75,140),0)  #
                        #color = (random.randint(90,104),random.randint(49,83),0)  # noir indestructible
                    self.grid[cy][cx] = color

    def create_map(self):
        """Dessine toute la carte une fois au démarrage"""
        for cy in range(self.cells_h):
            for cx in range(self.cells_w):
                color = self.grid[cy][cx]
                if color:
                    pygame.draw.rect(self.canva, color, self.rect_grid[cy][cx])

    def draw_map(self):
        """Dessine la map sur l'écran"""
        self.move_cells()
        self.screen.blit(self.canva, (0, 0))

    def get_circle_pattern(self, r_cells):
        """Retourne une liste d'offsets pour un rayon donné, pré-calculée"""
        if r_cells not in self.circle_patterns:
            pattern = []
            pattern_border = []
            for dy in range(-r_cells-1, r_cells + 2):
                for dx in range(-r_cells-1, r_cells + 2):
                    if dx*dx + dy*dy <= r_cells*r_cells:
                        pattern.append((dx, dy))
                    elif dx*dx + dy*dy <= (r_cells+1)*(r_cells+1):
                        pattern_border.append((dx, dy))
            self.circle_patterns[r_cells] = pattern
            self.border_patterns[r_cells] = pattern_border
        return self.circle_patterns[r_cells]
    

    def draw_rect(self, cx, cy):
        """Dessine un rectangle centré en (x, y)"""
        if 0 <= cx < self.cells_w and 0 <= cy < self.cells_h:
            pygame.draw.rect(self.canva, (255,0,0), self.rect_grid[cy][cx])

    def what_to_do(self,x,y):
        cx = x // self.cell_size
        cy = y // self.cell_size
        if 0 <= cx < self.cells_w and 0 <= cy < self.cells_h:
            if self.grid[cy][cx] is not None and self.grid[cy][cx] != (0, 0, 0):  # noir indestructible
                self.destroy_rect(cx,cy, 15)
            elif self.grid[cy][cx] is None:
                self.create_circle_sand(cx,cy,15)
        return "nothing"
    
    def create_circle_sand(self,x,y, r_cells):
        for dx,dy in self.get_circle_pattern(r_cells):
            cx = x + dx
            cy = y + dy
            if 0 <= cx < self.width and 0 <= cy < self.height:
                if 0 <= cx < self.cells_w and 0 <= cy < self.cells_h:
                    if self.grid[cy][cx] is None:
                        color = (random.randint(150,200),random.randint(75,140),0)  #
                        #color = (random.randint(90,104),random.randint(49,83),0)  # noir indestructible
                        self.grid[cy][cx] = color
                        pygame.draw.rect(self.canva, color, self.rect_grid[cy][cx])
                        self.cell_to_update.add((cx,cy))

    def destroy_rect(self, cx, cy, r_cells):
        """Détruit un cercle de rayon 'rayon' autour de (x, y)"""

        '''
                        for i in range(0,self.density[0]):

                            if y + 1 < self.cells_h and x +i >= 0 and self.grid[y + 1][x +i] is None:
                                self.update_cell(x,y,y+1,x+i)
                                # on ajoute les voisins à surveiller
                                if y - 1 >= 0:
                                    to_add.add((x, y - 1))

                                break
                        

                        for j in range(0,self.density[0]+1):
                            if x -j < self.cells_w:
                                to_add.add((x -j, y + 1))
                            if x +j < self.cells_w:
                                to_add.add((x +j, y + 1))

                            #if y + 1 < self.cells_h and x + 1 < self.cells_w:
                            #    to_add.add((x + 1, y + 1))
                            # bloquée, à supprimer'''

        for dx, dy in self.get_circle_pattern(r_cells):
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < self.cells_w and 0 <= ny < self.cells_h:
                if self.grid[ny][nx] is not None and self.grid[ny][nx] != (0, 0, 0):  # noir indestructible
                    # suppression dans la grille
                    self.grid[ny][nx] = None
                    # suppression graphique
                    self.canva.fill((255, 255, 255, 0), self.rect_grid[ny][nx])
        for dx,dy in self.border_patterns[r_cells]:
            if 0 <= cx+dx < self.cells_w and 0 <= cy+dy < self.cells_h:
                self.cell_to_update.add((cx+dx,cy+dy))
            #self.draw_rect(dx+cx,dy+cy)

    def move_cells(self):
        """Met à jour les cellules qui doivent tomber"""
        to_add = set()
        to_remove = set()

        for (x, y) in self.cell_to_update:
            #print(y,self.cells_h)
            if self.grid[y][x] is not None and self.grid[y][x] != (0, 0, 0):  # si la cellule existe et n'est pas noire
                
                if y + 1 < self.cells_h and self.grid[y + 1][x] is None:
                    self.update_cell(x, y, y+1,x)
                    # on ajoute les voisins à surveiller
                    if y - 1 >= 0:
                        to_add.add((x, y - 1))

                    if x + self.density[0] < self.cells_w:
                        to_add.add((x + self.density[0], y + 1))

                    if x - self.density[0] >= 0:
                        to_add.add((x - self.density[0], y + 1))

                    to_add.add((x, y + 1))

                else :

                    for i in range(1,self.density[0]+1):

                        if y + 1 < self.cells_h and x - i >= 0 and self.grid[y + 1][x - self.density[0]] is None:
                            self.update_cell(x,y,y+1,x-i)
                            # on ajoute les voisins à surveiller
                            if y - 1 >= 0:
                                to_add.add((x, y - 1))

                            for j in range(1,self.density[0]+1):
                                if x + i < self.cells_w:
                                    to_add.add((x + j, y + 1))
                                
                                to_add.add((x - j, y + 1))
                            break

                        elif y + 1 < self.cells_h and x + i < self.cells_w and self.grid[y + 1][x + i] is None:
                            self.update_cell(x,y,y+1,x+i)
                            # on ajoute les voisins à surveiller
                            if y - 1 >= 0:
                                to_add.add((x, y - 1))

                            for j in range(1,self.density[0]+1):
                                if x - 1 >= 0:
                                    to_add.add((x - j, y + 1))
                                
                                to_add.add((x + j, y + 1))
                            break
                
                if y - 1 >= 0: #A opti
                    to_add.add((x, y - 1))

                    #if y + 1 < self.cells_h and x + 1 < self.cells_w:
                    #    to_add.add((x + 1, y + 1))
                    # bloquée, à supprimer
                
                to_remove.add((x, y))

            else:
                # cellule vide => inutile de la garder
                to_remove.add((x, y))

        # maj des sets en une seule opération (rapide)
        self.cell_to_update -= to_remove
        self.cell_to_update |= to_add

    def add_to_list(self, x, y,l):
        """Ajoute une cellule à la liste des cellules à mettre à jour"""
        if 0 <= x < self.cells_w and 0 <= y < self.cells_h:
            l.add((x, y))

    def update_cell(self, x, y,newy,newx):
        """Fait tomber une cellule"""
        # échange dans la grille
        self.grid[newy][newx], self.grid[y][x] = self.grid[y][x], None

        # effacer ancienne position
        self.canva.fill((255, 255, 255, 0), self.rect_grid[y][x])
        # dessiner à la nouvelle position
        pygame.draw.rect(self.canva, self.grid[newy][newx], self.rect_grid[newy][newx])