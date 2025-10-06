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

            card.image = pygame.transform.rotate(card.image, 32.5 - i*9)  # Applique une rotation à la carte pour l'effet d'éventail

            self.playerHand.append(card)  # Ajoute la carte à la main du joueur avec son index

    def drawPlayerHand(self):
        """Affiche les cartes du player"""
        
        for idx, card in enumerate(self.playerHand):
            self.screen.blit(card.image,(self.Size[0]*(0.20 + idx/(self.deckSize*2)), (self.Size[1]*0.8 - self.Size[1]*(-abs(4-idx))/60)))  # Affiche la carte à la position calculée

    def drawAll(self):
        self.drawPlayerHand()