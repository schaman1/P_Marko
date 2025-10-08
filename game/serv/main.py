import pygame
from game import Game
#from D_CreateCards import load_cards

pygame.init()

# Set the title of the window
pygame.display.set_caption('P_Marko')

#Load cards :
#load_cards()

game = Game()
game.run()