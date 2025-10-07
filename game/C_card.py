import pygame

class Card:
    def __init__(self,power,color):
        self.cardName = f"{color}{power}"
        self.power = power
        self.color = color
        self.pos = (0,0)  # Position de la carte à l'écran

        self.angle = 0 #it a ne pas garder

        # Load the image
        self.image = pygame.image.load(f"assets/cards/{self.cardName}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 300))  # Resize the image to a standard size
        self.rot_img = self.image

        self.rect = self.image.get_rect()  # Get the rectangle of the image for positioning

    def draw(self,screen):
        """Draw the card on the screen at the given position"""
        screen.blit(self.rot_img, self.pos)

    def rotate_img(self):
        """Rotate the card image around it's center"""
        self.rot_img = pygame.transform.rotate(self.image,self.angle)
        #self.rect = self.rot_img.get_rect(center = self.image.get_rect(topleft = self.pos).center)