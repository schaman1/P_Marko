import pygame
import math
from D_CreateCards import cards

class Card:
    def __init__(self,power,color):
        self.cardName = f"{color}{power}"
        self.power = power
        self.color = color
        self.pos = (0,0)  # Position de la carte à l'écran
        self.ephPos = (0,0)  # Position éphémère pour les animations
        self.mouseOver = False  # Si la souris est au-dessus de la carte

        self.angle = 0 #it a ne pas garder

        # Load the image
        self.image = cards[self.cardName]
        self.image = pygame.transform.scale(self.image, (200, 300))  # Resize the image to a standard size
        self.rot_img = self.image

        self.rect = self.image.get_rect()  # Get the rectangle of the image for positioning

    def mouseOn(self,mouse_pos):
        """Retourne True si la souris est sur la carte"""
        return self.rect.collidepoint(mouse_pos)
    
    def findPos(self):

        if self.mouseOn(pygame.mouse.get_pos()):
            self.mouseOver = True
            return (self.pos[0], self.pos[1] - 30)  # Décale la carte vers le haut si la souris est dessus
        else:
            self.mouseOver = False
            return self.pos        

    def draw(self, screen):
        """Draw the card on the screen at the given position"""

        self.posEph = self.findPos()

        self.rect.center = self.posEph  # centre la carte sur la position voulue
        screen.blit(self.rot_img, self.rect.topleft )  # Décale la carte vers le haut si la souris est dessus

        