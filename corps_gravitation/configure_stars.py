import numpy as np
import math as m
import pygame

# Standard RGB color definitions
BLACK = (0, 0, 0)       # Noir
WHITE = (255, 255, 255) # Blanc
RED = (255, 0, 0)       # Rouge
GREEN = (0, 255, 0)     # Vert
BLUE = (150, 150, 255)      # Bleu
YELLOW = (255, 255, 0)  # Jaune
CYAN = (0, 255, 255)    # Cyan
TRON = (167, 208, 255)

init_data = [
    {"position":np.array([-1.496e8, 0], dtype=np.float64), "velocity":np.array([0, -297800], dtype=np.float64), "mass":1.989e28, "color":WHITE},
    {"position":np.array([1.496e8, 0], dtype=np.float64), "velocity":np.array([0, 297800], dtype=np.float64), "mass":1.989e28, "color":WHITE},
    {"position":np.array([1e8, -2.5e8], dtype=np.float64), "velocity":np.array([-47000, -1000], dtype=np.float64), "mass":1.989e26, "color":WHITE},
    {"position":np.array([-1.496e8, 0], dtype=np.float64), "velocity":np.array([47000, 1000], dtype=np.float64), "mass":1.989e26, "color":WHITE},

]

def crant_bar( win, mouse_pos, click, x, y, choices, default,length, width, color):  ## Selection bar
    if not hasattr(crant_bar, "val"):
        crant_bar.val = default*length/(choices)
    init = pygame.Rect(x, y, length, width)
    pygame.draw.rect(win, color, init, border_radius=2)

    init_black = pygame.Rect(x+crant_bar.val+3, y+3, length-crant_bar.val-6, width-6)
    pygame.draw.rect(win, BLACK, init_black, border_radius=4)

    if init.collidepoint(mouse_pos):
        if click[0]==1:
            for i in range(choices):
                if mouse_pos[0]> x+i*(length/choices) and mouse_pos[0]< x+(i+1)*(length/choices):
                    crant_bar.val = (i+1)*(length/choices)
    return int(crant_bar.val/length*choices)

def draw_text(win, text, font_size, position, color):
    font = pygame.font.SysFont('courier new', font_size)
    font.set_bold(True)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    win.blit(text_surface, text_rect)

class Star:
    def __init__(self, position, velocity, mass, color):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.color = color

    def draw(self, win, WIDTH, HEIGHT):
        x = self.position[0] * 1e-6 + WIDTH / 2
        y = self.position[1] * 1e-6 + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x,y), 8)

stars = []
previous = 0
### creation of the menu parameters
def configure_stars(win, mouse_pos, click, stars_number, WIDTH, HEIGHT):
    global previous
    global stars
    par_size = HEIGHT/(stars_number+3)

    if previous != stars_number:
        for data in init_data[:stars_number+1]:
            star = Star(
                position=data["position"],
                velocity=data["velocity"],
                mass=data["mass"],
                color=data["color"]
            )
            stars.append(star)
        print(stars[0].position) 


    for i in range(stars_number+1):
        x = crant_bar(win, mouse_pos, click, WIDTH-250, par_size*(i+1)+160, 200, (100/1e9)*stars[i].position[0]+100, 200, 12, WHITE)
        y = crant_bar(win, mouse_pos, click, WIDTH-250, par_size*(i+1)+20+160, 200, (100/1e9)*stars[i].position[1]+100, 200, 12, WHITE)
        print(x,y)
        print(stars[i].position[0])
        stars[i].position = np.array([1e9/100*(x-100), 1e9/100*(y-100)], dtype=np.float64)
        
    
    previous = stars_number
