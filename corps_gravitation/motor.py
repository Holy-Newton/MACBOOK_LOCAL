import numpy as np
import math as m
import pygame
from menu import menu
from configure_stars import Star

pygame.init()
WIDTH, HEIGHT = 1200, 900

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitational Trajectory Simulation by Holy-Newton")


# CONSTANT
epsilon = 2e6  ### epsilon is the "softening" to avoid singularities. (logical)#
G = 6.67430e-9
# Commonly used colors in programming
BLACK = (0, 0, 0)       # Noir
WHITE = (255, 255, 255) # Blanc
RED = (255, 0, 0)       # Rouge
GREEN = (0, 255, 0)     # Vert
BLUE = (150, 150, 255)      # Bleu
YELLOW = (255, 255, 0)  # Jaune
CYAN = (0, 255, 255)    # Cyan
TRON = (167, 208, 255)


### _______________MAIN()________________________
def main(win):
    quit_menu = False
    epsilon = 2e6  ### epsilon is the "softening" to avoid singularities. (logical)#
    G = 6.67430e-9  
    stars = menu(win, WIDTH, HEIGHT)
    
    run = True
    clock = pygame.time.Clock()
    dt = 0.7

#-----------------### LOOP ###------------------

    while run:
        clock.tick(100) 
        win.fill(BLACK) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if quit_menu:
            run = False

        for star in stars:
            star.new_position(dt, stars, G, epsilon)
            star.draw(win, WIDTH, HEIGHT)
        pygame.display.update()

    pygame.quit()

main(win)