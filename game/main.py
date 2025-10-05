import pygame
from C_game import Game

pygame.init()

# Set the title of the window
pygame.display.set_caption('P_Marko')

game = Game()
game.run()