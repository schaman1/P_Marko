import pygame
from random import shuffle

class InGame:

    def __init__(self,screen,screenSize,font,deck):
        self.screen = screen
        self.Size = screenSize
        self.font = font
        self.deckSize = 8

        self.deck = deck
        self.availableCards = list(deck)  # Cartes disponibles dans le jeu
        self.playerHand = []  # Cartes en main du joueur
            
    def createHand(self):
        """Crée la main du joueur"""
        shuffle(self.availableCards)

        for i in range(self.deckSize):
            card = self.availableCards.pop()
            card.pos = (self.Size[0]//2 + (i - self.deckSize//2) * 50, self.Size[1]*0.9)
            self.playerHand.append(card)

    def drawPlayerHand(self):
        """Affiche toutes les cartes du joueur"""


        for card in self.playerHand:
            card.draw(self.screen)

    def drawAll(self):
        self.drawPlayerHand()