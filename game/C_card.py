import pygame

class Card:
    def __init__(self,power,color):
        self.cardName = f"{color}{power}"
        self.power = power
        self.color = color

        # Load the image
        self.image = pygame.image.load(f"assets/cards/{self.cardName}.png").convert_alpha()

        self.rect = self.image.get_rect()  # Get the rectangle of the image for positioning