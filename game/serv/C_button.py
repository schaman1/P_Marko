import pygame

class Button:
    def __init__(self,rect,color,text,font,border=10):
        self.rect = rect
        self.color = color
        self.border = border
        self.text = text
        self.font = font

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect,border_radius = self.border)
        # Centrer le texte dans le rectangle
        text = self.font.render(self.text, True, (0,0,0))  # True = anti-aliasing
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)