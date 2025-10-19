import pygame
from read_map import Read_map
#from D_CreateCards import load_cards

pygame.init()

# Set the title of the window
pygame.display.set_caption('P_Marko')

#Load cards :
#load_cards()

#def init():
# Set up the display (width, height)
screen = pygame.display.set_mode((pygame.display.Info().current_w,pygame.display.Info().current_h),pygame.FULLSCREEN | pygame.SCALED)
screenSize = (screen.get_width(),screen.get_height())

#ecriture
font = pygame.font.SysFont(None, 48)

bg = pygame.image.load("../game/assets/bg1.png").convert()
fps = 1000
fpsClock = pygame.time.Clock()

def run():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                map.what_to_do(x, y)

        screen.blit(bg, (0, 0))
        #screen.fill((255, 255, 255))

        map.draw_map()

        # Update the display
        pygame.display.flip()

        #fpsClock.tick(fps) / 1000

        #self.dt = self.fpsClock.tick(self.fps) / 1000

    pygame.quit()

map = Read_map("../game/assets/map_1.png",screen,6)

run()

