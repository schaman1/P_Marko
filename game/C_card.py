import pygame
import math
from D_CreateCards import cards

class Card:
    def __init__(self,power,color):
        self.cardName = f"{color}{power}"
        self.power = power
        self.color = color
        self.pos = (0,0)  # Position de la carte à l'écran

        self.angle = 0 #it a ne pas garder

        # Load the image
        self.image = cards[self.cardName]
        self.image = pygame.transform.scale(self.image, (200, 300))  # Resize the image to a standard size
        self.rot_img = self.image

        self.rect = self.image.get_rect()  # Get the rectangle of the image for positioning

    def draw(self, screen):
        """Draw the card on the screen at the given position"""
        self.rect.center = self.pos  # centre la carte sur la position voulue
        screen.blit(self.rot_img, self.rect.topleft)

    def rotate_around_pivot(self, pivot, angle):
        """
        Fait tourner la carte autour d’un pivot global (ex: bas de l’écran)
        pivot : (x, y)
        angle : en degrés
        """
        rad = math.radians(angle)

        # Point de référence (le centre actuel de la carte)
        cx, cy = self.pos

        # Calcul de la nouvelle position après rotation autour du pivot
        x = math.cos(rad) * (cx - pivot[0]) - math.sin(rad) * (cy - pivot[1]) + pivot[0]
        y = math.sin(rad) * (cx - pivot[0]) + math.cos(rad) * (cy - pivot[1]) + pivot[1]

        # Rotation de l’image
        self.rot_img = pygame.transform.rotate(self.image, angle)

        # Mise à jour du rect centré sur la nouvelle position
        self.rect = self.rot_img.get_rect(center=(x, y))
