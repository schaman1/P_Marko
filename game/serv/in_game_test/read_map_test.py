import pygame, numpy as np
from serv.in_game.particles import Sand,Wood, Water, Fire

class Read_map:
    def __init__(self,filename,size,canva_size):
        self.width = canva_size[0]
        self.height = canva_size[1]
        self.cell_size = size
        self.cells_w = self.width // self.cell_size
        self.cells_h = self.height // self.cell_size

        self.type = {"EMPTY":0,"SAND":1,"WATER":2,"WOOD":3,"FIRE":4}

        self.map = pygame.image.load(filename).convert()
        self.map = pygame.transform.scale(self.map, (self.width, self.height))

        self.grid_type = np.zeros((self.cells_h, self.cells_w), dtype=np.uint8)
        self.grid_temp = np.zeros((self.cells_h, self.cells_w), dtype=np.uint8) #Temperature
        self.grid_color = np.zeros((self.cells_h,self.cells_w,4), dtype=np.uint8)

        self.create_map()

    def create_map(self):
        img_np = pygame.surfarray.array3d(self.map)  # shape = (W, H, 3)
        img_np = np.transpose(img_np, (1,0,2))   # swap axes pour (H,W,3)

        self.grid_color[:,:] = [0,0,0,0]

        # on prend le pixel en haut à gauche de chaque bloc
        grid_pixels = img_np[0:self.height:self.cell_size, 0:self.width:self.cell_size]  # shape = (grid_h, grid_w, 3)
        mask_Sand = (grid_pixels[:,:,0] == 255) & (grid_pixels[:,:,1] == 255) & (grid_pixels[:,:,2] == 0)
        mask_Water = (grid_pixels[:,:,0] == 0) & (grid_pixels[:,:,1] == 0) & (grid_pixels[:,:,2] == 255)
        mask_Wood = (grid_pixels[:,:,0] == 0) & (grid_pixels[:,:,1] == 0) & (grid_pixels[:,:,2] == 0)
        mask_Fire = (grid_pixels[:,:,0] == 255) & (grid_pixels[:,:,1] == 0) & (grid_pixels[:,:,2] == 0)

        mask_Sand[0,0] = True

        self.grid_type[mask_Sand]  = self.type["SAND"]
        self.grid_type[mask_Water] = self.type["WATER"]
        self.grid_type[mask_Fire]  = self.type["FIRE"]
        self.grid_type[mask_Wood] = self.type["WOOD"]

        self.grid_color[mask_Sand] = self.random_color_sand(mask_Sand)
        self.grid_color[mask_Water] = self.random_color_water(mask_Water)
        self.grid_color[mask_Wood] = self.random_color_wood(mask_Wood)
        self.grid_color[mask_Fire] = self.random_color_fire(mask_Fire)

    def random_color_sand(self,mask_sand):
        num_cells = np.sum(mask_sand)  # nombre de cellules à colorer
        r = np.random.randint(150, 200, size=num_cells, dtype=np.uint8)
        g = np.random.randint(75, 140, size=num_cells, dtype=np.uint8)
        b = np.zeros(num_cells,dtype=np.uint8)
        a = np.full(num_cells, 255, dtype=np.uint8)
        return np.stack([r, g, b,a], axis=1)
    
    def random_color_water(self,mask_water):
        num_cells = np.sum(mask_water)  # nombre de cellules à colorer
        r = np.random.randint(0, 20, size=num_cells, dtype=np.uint8)
        g = np.random.randint(0, 20, size=num_cells, dtype=np.uint8)
        b = np.random.randint(200, 255, size=num_cells, dtype=np.uint8)
        a = np.full(num_cells, 255, dtype=np.uint8)
        return np.stack([r, g, b,a], axis=1)
    
    def random_color_wood(self,mask_wood):
        num_cells = np.sum(mask_wood)  # nombre de cellules à colorer
        r = np.random.randint(78, 88, size=num_cells, dtype=np.uint8)
        g = np.random.randint(31, 41, size=num_cells, dtype=np.uint8)
        b = np.zeros(num_cells,dtype=np.uint8)
        a = np.full(num_cells, 255, dtype=np.uint8)
        return np.stack([r, g, b,a], axis=1)
    
    def random_color_fire(self,mask_fire):
        num_cells = np.sum(mask_fire)  # nombre de cellules à colorer
        r = np.random.randint(180, 256, size=num_cells, dtype=np.uint8)
        g = np.random.randint(0, 20, size=num_cells, dtype=np.uint8)
        b = np.zeros(num_cells,dtype=np.uint8)
        a = np.full(num_cells, 255, dtype=np.uint8)
        return np.stack([r, g, b,a], axis=1)
    
    def return_all(self):
        # masque des cellules actives (non vide)
        mask_active = (self.grid_type != self.type["EMPTY"])  # bool array

        # récupérer les coordonnées (y,x)
        ys, xs = np.where(mask_active)

        # récupérer les couleurs correspondantes
        colors_active = self.grid_color[ys, xs]  # shape = (num_active, 3) ou (num_active,4)

        # créer la liste (x, y, color)
        return np.column_stack((xs, ys, colors_active)).tolist()#[(int(x), int(y), tuple(int(v)for v in c)) for x, y, c in zip(xs, ys, colors_active)]
    
    def return_sand(self):

        mask_sand = (self.grid_type == self.type["SAND"])
        falling = self.empty_sand(mask_sand,0,1)
        moved_cells = self.move(falling,0,1)

        mask_sand = (self.grid_type == self.type["SAND"])
        falling = self.empty_sand(mask_sand,1,1)
        moved_cells += self.move(falling,1,1)

        mask_sand = (self.grid_type == self.type["SAND"])
        falling = self.empty_sand(mask_sand,-1,1)
        moved_cells += self.move(falling,-1,1)

        return moved_cells
    
    def empty_sand(self,mask_sand,dx,dy):
        below_empty = np.zeros_like(self.grid_type, bool)

        bx = -dx if dx != 0 else None

        below_empty[:-dy, :bx] = (
            (self.grid_type[dy:, dx:] == self.type["EMPTY"]) |
            (self.grid_type[dy:, dx:] == self.type["WATER"])
        )
        falling = mask_sand & below_empty
        return falling[:-dy,:bx]
    
    def move(self,falling,dx,dy):
        # MAJ types

        bx = -dx if dx != 0 else None

        self.grid_type[:-dy, :bx][falling] = self.type["EMPTY"]
        self.grid_type[dy:,dx:][falling] = self.type["SAND"]

        # échange couleurs
        tmp = self.grid_color[:-dy, :bx][falling].copy()
        self.grid_color[:-dy, :bx][falling] = self.grid_color[dy:, dx:][falling]
        self.grid_color[dy:, dx:][falling] = tmp

        ys, xs = np.where(falling)
        old_colors = self.grid_color[:-dy, :bx][falling]
        new_ys = ys + dy
        new_xs = xs + dx
        new_colors = self.grid_color[dy:, dx:][falling]

        return (
            np.column_stack((xs, ys, old_colors)).tolist() +
            np.column_stack((new_xs, new_ys, new_colors)).tolist()
        )

'''class Read_map:
    def __init__(self, filename, size,canva_size):
        self.width = canva_size[0]
        self.height = canva_size[1]
        self.cell_size = size
        self.cells_w = self.width // self.cell_size
        self.cells_h = self.height // self.cell_size

        self.map = pygame.image.load(filename).convert()
        self.map = pygame.transform.scale(self.map, (self.width, self.height))

        self.grid = [[None for _ in range(self.cells_w)] for _ in range(self.cells_h)]
        
        # sets plutôt que listes = O(1) lookup, remove, add
        self.cell_to_update = set()
        self.circle_patterns = {}
        self.border_patterns = {}

        self.read_map()

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
                    if color == (255, 255, 0):  # sable
                        self.grid[cy][cx] = Sand(cx,cy)
                        self.cell_to_update.add((cx,cy))
                        #color = (random.randint(90,104),random.randint(49,83),0)  # noir indestructible
                    elif color == (0, 0, 255):  # eau
                        #self.grid[cy][cx] = Sand(cx,cy)
                        self.grid[cy][cx] = Water(cx,cy,self.cells_w,self.cells_h)
                        self.cell_to_update.add((cx,cy))
                        #color = (0,0,255)
                    elif color == (255,0,0):
                        self.grid[cy][cx] = Fire(cx,cy)
                        self.cell_to_update.add((cx,cy))
                    else :
                        self.grid[cy][cx] = Wood(cx,cy)  # noir indestructible

    def return_map(self):
        """Dessine la map sur l'écran"""
        
        return self.move_cells()

    def move_cells(self):
        """Met à jour les cellules qui doivent tomber"""

        to_remove = set()
        to_add = set()
        to_update = []

        for (x, y) in self.cell_to_update:
            
            if self.grid[y][x] is not None and self.grid[y][x].__class__.__name__ != "Wood":  # si la cellule existe et n'est pas noire
                
                moved, (newx, newy), new_set = self.grid[y][x].update_position(self.grid,self.cells_h,self.cells_w)

                if moved is None:
                    self.destroy_cell(x,y)
                    to_update.append((x,y,(255,255,255,0)))
                    
                    if new_set is not None :
                        to_add |= new_set

                elif moved is True: 
                        if newx is not None:
                            if self.grid[newy][newx] is None :
                                to_update.append((x,y,(255,255,255,0)))
                            else :
                                to_update.append((x,y,self.grid[newy][newx].color))
                            #else 
                            to_update.append((newx,newy,self.grid[y][x].color))
                            self.update_cell(x,y,newx,newy)

                        if new_set is not None :
                            to_add |= new_set                 
                
            to_remove.add((x, y))

        # maj des sets en une seule opération (rapide)
        self.cell_to_update -= to_remove
        self.cell_to_update |= to_add
        return to_update

    def add_to_list(self, x, y,l):
        """Ajoute une cellule à la liste des cellules à mettre à jour"""
        if 0 <= x < self.cells_w and 0 <= y < self.cells_h:
            l.add((x, y))

    def destroy_cell(self, x, y):
        """Détruit une cellule"""
        # suppression dans la grille
        self.grid[y][x] = None

    def update_cell(self, x, y,newx,newy):
        """Fait tomber une cellule"""
        # échange dans la grille

        self.grid[newy][newx], self.grid[y][x] = self.grid[y][x], self.grid[newy][newx]'''