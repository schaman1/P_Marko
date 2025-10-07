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
        """Crée la main du joueur avec effet éventail réaliste"""
        shuffle(self.availableCards)

        # Pivot commun (point depuis lequel on "tient" les cartes)
        pivot = (self.Size[0] / 2, self.Size[1] * 1.15)

        # Configuration de l’éventail
        angle_start = 30                     # angle de la première carte (à gauche)
        angle_step = -60 / (self.deckSize - 1) # écart d’angle entre les cartes
        spread = 200                          # largeur de l’éventail (décalage horizontal)
        lift = 30                             # petit décalage vertical pour la courbe

        for i in range(self.deckSize):
            card = self.availableCards.pop()

            # Calcul de l’angle propre à cette carte
            card.angle = angle_start + i * angle_step

            # Décalage latéral pour étaler les cartes
            offset_x = (i - (self.deckSize - 1) / 2) * (spread / self.deckSize)
            offset_y = -abs(i - (self.deckSize - 1) / 2) * lift / (self.deckSize / 2)

            # Position de base avant rotation
            base_pos = (pivot[0] + offset_x, self.Size[1] * 0.65 + offset_y)
            card.pos = base_pos

            # Appliquer la rotation autour du pivot
            card.rotate_around_pivot(pivot, card.angle)

            self.playerHand.append(card)

    def drawPlayerHand(self):
        """Affiche toutes les cartes du joueur"""
        # Pour un bel ordre d’affichage, on dessine de la carte la plus inclinée à la plus droite
        for card in sorted(self.playerHand, key=lambda c: c.angle):
            card.draw(self.screen)

    def drawAll(self):
        self.drawPlayerHand()