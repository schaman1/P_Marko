import pygame


def a_state(state,screen):

    if state == "menu":
        pygame.draw.rect(screen, (255, 0, 0), (0, 0, 100, 100))