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


def crant_bar( win, mouse_pos, click, x, y, choices, default,length, width, color, color2, key):  ## Selection bar
    if not hasattr(crant_bar, "val"):
        crant_bar.val = {}

    if key not in crant_bar.val:
        crant_bar.val[key] = default*length/choices
        print(1)
    else:
        default = crant_bar.val[key] * choices/length
        print(2)

    init_bg = pygame.Rect(x-2, y-2, length+4, width+4)
    pygame.draw.rect(win, color2, init_bg, border_radius=2)

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

def light_draw_text(win, text, position, color, font):
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
    Font = pygame.font.SysFont('courier new', 16)

    Lenght_bar = 300
    OFFSET = Lenght_bar/2
    POSITION = 1e9
    Pos_scale = POSITION / OFFSET
    Vel_scale = 1e6 / OFFSET
    Mass_scale = 1e27
    

    
    stars_number = int( crant_bar(win, mouse_pos, click, WIDTH- Lenght_bar - 50, 250, 3,1, Lenght_bar, 20, WHITE, RED, key = f"star_number") + 1)
    draw_text(win, f"Stars number : {stars_number}", 20, (WIDTH- Lenght_bar/2 - 50, 230), RED)
    par_size = HEIGHT/(stars_number+3)

    global previous
    global stars

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
            
    ### ----------  PARAMETERS  ---------------

    for i, star in enumerate(stars):
        draw_text(win, f"Star {i+1}", 20, (WIDTH-Lenght_bar-50+Lenght_bar/2, par_size*(i+1)+160), WHITE)

        x = crant_bar(win, mouse_pos, click, WIDTH-Lenght_bar-50, par_size*(i+1)+180, 200, stars[i].position[0]/Pos_scale+OFFSET, Lenght_bar, 12, WHITE, TRON, key = f"star{i}_x")
        formatted_x = f"x: {Pos_scale*(x-OFFSET)/1000:.3e}"
        light_draw_text(win, formatted_x+" km", (WIDTH-Lenght_bar-180, par_size*(i+1) + 188), WHITE, Font)
        
        y = crant_bar(win, mouse_pos, click, WIDTH-Lenght_bar-50, par_size*(i+1)+20+180, 200, stars[i].position[1]/Pos_scale+OFFSET, Lenght_bar, 12, WHITE,TRON, key = f"star{i}_y")
        formatted_y = f"y: {Pos_scale*(y-OFFSET)/1000:.3e}"
        light_draw_text(win, formatted_y+" km", (WIDTH-Lenght_bar-180, par_size*(i+1) + 20+ 188), WHITE, Font)
        
        Vx = crant_bar(win, mouse_pos, click, WIDTH-Lenght_bar-50, par_size*(i+1)+40+180, 200, stars[i].velocity[0]/Vel_scale+OFFSET, Lenght_bar, 12, WHITE, TRON, key = f"star{i}_Vx")
        formatted_Vx = f"Vx: {Vel_scale*(Vx-OFFSET)/1000:.3e}"
        light_draw_text(win, formatted_Vx + " km/s", (WIDTH-Lenght_bar-180, par_size*(i+1) + 40+ 188), WHITE, Font)

        Vy = crant_bar(win, mouse_pos, click, WIDTH-Lenght_bar-50, par_size*(i+1)+60+180, 200, stars[i].velocity[1]/Vel_scale+OFFSET, Lenght_bar, 12, WHITE,TRON, key = f"star{i}_Vy")
        formatted_Vy = f"Vy: {Vel_scale*(Vy-OFFSET)/1000:.3e}"
        light_draw_text(win, formatted_Vy + " km/s", (WIDTH-Lenght_bar-180, par_size*(i+1)+ 60 + 188), WHITE, Font)
        
        mass = crant_bar(win, mouse_pos, click, WIDTH-Lenght_bar-50, par_size*(i+1)+80+180, 200, stars[i].mass/Mass_scale, Lenght_bar, 12, WHITE, TRON, key = f"star{i}_mass")
        formatted_mass = f"Mass: {mass*Mass_scale:.3e}"
        light_draw_text(win, formatted_mass + " kg", (WIDTH-Lenght_bar-180, par_size*(i+1)+80+188), WHITE, Font)

        stars[i].position = np.array([Pos_scale*(x-OFFSET), Pos_scale*(y-OFFSET)], dtype=np.float64)
        stars[i].velocity = np.array([Vel_scale*(Vx-OFFSET), Vel_scale*(Vy-OFFSET)], dtype=np.float64)
        stars[i].mass = mass*Mass_scale
        #if abs(Vel_scale*(Vy-OFFSET)/1000) or abs(Vel_scale*(Vx-OFFSET)/1000) > 300000000:
        #    draw_text(win, "STUPID BOY, not more that 299 458 792 km/s !!!", 35, (WIDTH/2, HEIGHT/2), RED)

    ### --------------  VISUALISATION  ----------------

    VW = WIDTH/2.3
    VH = HEIGHT/1.87
    Scale_W = VW/POSITION
    Scale_H = VH/POSITION
    x_center = VW /2 + 58
    y_center = VH /2 + HEIGHT/5+44
    visu_back = pygame.Rect(58, HEIGHT/5+40, VW, VH)
    pygame.draw.rect(win, TRON, visu_back, border_radius=10)

    visu_dark = pygame.Rect(62, HEIGHT/5+44, VW-8, VH-8)
    pygame.draw.rect(win, BLACK, visu_dark, border_radius=10)

    for star in stars:
        pygame.draw.circle(win, WHITE, (x_center + Scale_W*star.position[0], y_center + Scale_H*star.position[1]), 5)











    previous = stars_number
