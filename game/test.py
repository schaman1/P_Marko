import pygame

# Initialize Pygame
pygame.init()

# Set up the display (width, height)
screen = pygame.display.set_mode((800, 600))

# Set the title of the window
pygame.display.set_caption('My First Pygame Window')

# Main loop to keep the window running
running = True
while running:
    for event in pygame.event.get():
    # Check for quit event
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (RGB format)
    screen.fill((0, 128, 255)) # Blue background

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()