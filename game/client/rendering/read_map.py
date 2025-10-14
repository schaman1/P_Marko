import pygame
import math

class Read_map:
    def __init__(self, filename, screen):
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.cell_size = 4
        self.cells_w = self.width // self.cell_size
        self.cells_h = self.height // self.cell_size

        self.map = pygame.image.load(filename).convert()
        self.map = pygame.transform.scale(self.map, (self.width, self.height))
        self.canva = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.screen = screen

        # grille binaire + couleurs
        self.grid = [[None for _ in range(self.cells_w)] for _ in range(self.cells_h)]

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
                    self.grid[cy][cx] = color  # stockage direct dans la grille

    def create_map(self):
        """Dessine toute la carte une fois au démarrage"""
        for cy in range(self.cells_h):
            for cx in range(self.cells_w):
                color = self.grid[cy][cx]
                if color:
                    rect = pygame.Rect(cx * self.cell_size, cy * self.cell_size,
                                       self.cell_size, self.cell_size)
                    pygame.draw.rect(self.canva, color, rect)

    def draw_map(self):
        """Dessine la map sur l'écran"""
        self.screen.blit(self.canva, (0, 0))

    def destroy_rect(self, x, y, r_cells):
        """Détruit un cercle de rayon 'rayon' autour de (x, y)"""
        cx = x // self.cell_size
        cy = y // self.cell_size

        for dy in range(-r_cells, r_cells + 1):
            for dx in range(-r_cells, r_cells + 1):
                if dx**2 + dy**2 <= r_cells**2:
                    nx = cx + dx
                    ny = cy + dy
                    if 0 <= nx < self.cells_w and 0 <= ny < self.cells_h:
                        if self.grid[ny][nx] is not None and self.grid[ny][nx] != (0, 0, 0):
                            # suppression dans la grille
                            self.grid[ny][nx] = None
                            # suppression graphique
                            rect = pygame.Rect(nx * self.cell_size,
                                               ny * self.cell_size,
                                               self.cell_size,
                                               self.cell_size)
                            self.canva.fill((255, 255, 255,0), rect)