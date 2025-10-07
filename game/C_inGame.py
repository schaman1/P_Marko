import pygame
from random import shuffle

class InGame:

    def __init__(self,screen,screenSize,font,deck):
        self.screen = screen
        self.Size = screenSize
        self.font = font
        self.deckSize = 8

        self.deck = deck
        self.availableCards = self.deck  # Cartes disponibles dans le jeu
        self.playerHand = []  # Cartes en main du joueur
            
    def createHand(self):
        """Create the hand of the player"""
        shuffle(self.availableCards)

        for i in range(self.deckSize):

            card = self.availableCards.pop()  # Retire une carte du deck
            card.pos = (self.Size[0]*(0.20 + i/(self.deckSize*2)), (self.Size[1]*0.6 - self.Size[1]*(-abs(3.5-i))/60))
            card.angle = 32.5 - i*9
            card.rotate_img()
            #card.image = pygame.transform.rotate(card.image, 32.5 - i*9)  # Applique une rotation à la carte pour l'effet d'éventail

            self.playerHand.append(card)  # Ajoute la carte à la main du joueur avec son index

    def drawPlayerHand(self):
        """Affiche les cartes du player"""
        
        for card in self.playerHand :
            card.draw(self.screen)

    def drawAll(self):
        self.drawPlayerHand()