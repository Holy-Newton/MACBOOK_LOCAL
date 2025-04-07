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



def crant_bar( win, mouse_pos, click, x, y, choices, default,length, width, color, key):  ## Selection bar
    if not hasattr(crant_bar, "val"):
        crant_bar.val = {}

    if key not in crant_bar.val:
        crant_bar.val[key] = default*length/choices
        print(1)
    else:
        default = crant_bar.val[key] * choices/length
        print(2)


    init = pygame.Rect(x, y, length, width)
    pygame.draw.rect(win, color, init, border_radius=2)

    init_black = pygame.Rect(x+crant_bar.val[key]+3, y+3, length-crant_bar.val[key]-6, width-6)
    pygame.draw.rect(win, BLACK, init_black, border_radius=4)

    if init.collidepoint(mouse_pos):
        if click[0]==1:
            for i in range(choices):
                if (x+(i+1)*(length/choices)) >= mouse_pos[0] >= (x+i*(length/choices)):
                    crant_bar.val[key] = (i+1)*(length/choices)

    return crant_bar.val[key]/length*choices



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

stars = []
previous = 0
### creation of the menu parameters
def configure_stars(win, mouse_pos, click, WIDTH, HEIGHT):
    

    stars_number = int( crant_bar(win, mouse_pos, click, WIDTH- 250, 250, 3,1, 200, 20, WHITE, key = f"star_number") + 1)

    global previous
    global stars

    par_size = HEIGHT/(stars_number+3)
    Pos_scale = 1e9 / 100
    OFFSET = 100

    

    if previous != stars_number:
        stars = []
        for data in init_data[:stars_number]:
            star = Star(
                position=data["position"],
                velocity=data["velocity"],
                mass=data["mass"],
                color=data["color"]
            )
            stars.append(star)
            '''
            index = len(stars) - 1
            key_x = f"star{index}_x"
            key_y = f"star{index}_y"
            stars.append(star)
            if key_x not in crant_bar.val:
                crant_bar.val[key_x] = star.position[0]
            if key_y not in crant_bar.val:
                crant_bar.val[key_y] = star.position[1]
            '''


    for star in stars:
        i = stars.index(star)
        x = crant_bar(win, mouse_pos, click, WIDTH-250, par_size*(i+1)+160, 200, stars[i].position[0]/Pos_scale+OFFSET, 200, 12, WHITE,key = f"star{i}_x")
        y = crant_bar(win, mouse_pos, click, WIDTH-250, par_size*(i+1)+20+160, 200, stars[i].position[1]/Pos_scale+OFFSET, 200, 12, WHITE,key = f"star{i}_y")
        #print(x,y)
        stars[i].position = np.array([Pos_scale*(x-OFFSET), Pos_scale*(y-OFFSET)], dtype=np.float64)
        print(stars[i].position[0])
    
    previous = stars_number
