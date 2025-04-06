import numpy as np
import math as m
import pygame

pygame.init()
WIDTH, HEIGHT = 1200, 900
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitational Trajectory Simulation by Holly Newton")


# CONSTANT
epsilon = 2e6  ### epsilon is the "softening" to avoid singularities. (logical)#
G = 6.67430e-9
teta = 0.1
fact = 1
# Commonly used colors in programming
BLACK = (0, 0, 0)       # Noir
WHITE = (255, 255, 255) # Blanc
RED = (255, 0, 0)       # Rouge
GREEN = (0, 255, 0)     # Vert
BLUE = (150, 150, 255)      # Bleu
YELLOW = (255, 255, 0)  # Jaune
CYAN = (0, 255, 255)    # Cyan
TRON = (167, 208, 255)

class Star:
    def __init__(self, name, mass, radius, color, position, velocity, trace_val):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.color = color
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.orbit = []
        if trace_val: self.trace = []

    def draw(self, win):
        x = self.position[0] * 1e-6 + WIDTH / 2
        y = self.position[1] * 1e-6 + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x,y), self.radius)



    def acceleration(self, other):
        r = np.linalg.norm(other.position - self.position)
        a = G * other.mass * (other.position - self.position) / ((r)**2 + epsilon**2)**(3/2)
        return a
    
    def new_position(self, dt, star_system):
        OTHERS = star_system.copy()
        OTHERS.remove(self)
        a_tot = np.array([0, 0], dtype=np.float64)
        for other in OTHERS:
            a_tot += self.acceleration(other)
        self.velocity += a_tot * dt
        self.position += self.velocity * dt


### _______________MENU()________________________

def draw_text(win, text, font_size, position, color):
    font = pygame.font.SysFont('courier new', font_size)
    font.set_bold(True)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    win.blit(text_surface, text_rect)

def chargement(x , y, teta, fact):
    n = int(teta/(2*m.pi) * 255)
    a,b = x,y
    radius = 14
    if fact == 1:
        x += radius * np.cos(teta)
        y += radius * np.sin(teta)
        x1 = a+(-radius) * np.cos(teta)
        y1 = b+(-radius) * np.sin(teta)
    else:
        x += radius * np.cos(2*m.pi-teta)
        y += radius * np.sin(2*m.pi-teta)
        x1 = a+(-radius) * np.cos(-teta)
        y1 = b+(-radius) * np.sin(-teta)
    pygame.draw.circle(win, (255-n/2, 255-n, 255), (x,y), 10)
    pygame.draw.circle(win, (n/1.3, 40, 90), (x1,y1), 10)
    

def menu():
    global quit_menu
    clock = pygame.time.Clock()
    run = True
    WB, HB = 500,100
    global teta
    global fact
    while run:
        
        ### CHARGEMENT
        if teta >= 2*m.pi or teta <= 0:
            fact = -fact
            teta += fact*0.1
        else: teta += fact*0.1
        clock.tick(60)
        win.fill(BLACK)

        ### TITLE

        title_square = pygame.Rect(58, 57, WIDTH*0.90, 100)
        title_square1 = pygame.Rect(58+4, 57+4, WIDTH*0.90-8, 92)
        pygame.draw.rect(win, TRON, title_square, border_radius=10)
        pygame.draw.rect(win, BLACK, title_square1, border_radius=10)
        font = pygame.font.SysFont('courier new', 29)
        font.set_underline(True)
        font.set_bold(True)
        text = font.render("==Gravitational Trajectory Simulation====@Holy_Newton==", 1, TRON)
        win.blit(text, (WIDTH/2 - text.get_width()/2, 130 - text.get_height()/1))


        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # START BUTTON
        
        start_but = pygame.Rect(550/2-WB/2, HEIGHT-150-HB/2+50,WB, HB)
        start_but2 = pygame.Rect(550/2-WB/2+4, HEIGHT-150+4-HB/2+50, WB-8, HB-8)
        pygame.draw.rect(win, TRON, start_but, border_radius=10)
        pygame.draw.rect(win, BLACK, start_but2, border_radius=10)
        draw_text(win, "Start Simulation", 35, (250, HEIGHT-100), TRON)

        if start_but.collidepoint(mouse_pos):
            WB, HB = 515,115
            draw_text(win, "Start Simulation", 39, (250, HEIGHT-100), TRON)        
            if click[0]:
                draw_text(win, "Start Simulation", 29, (250, HEIGHT-100), TRON)
                WB, HB = 485,85
        else:
            draw_text(win, "Start Simulation", 35, (250, HEIGHT-100), TRON)
            WB, HB = 500,100
        

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    if start_but.collidepoint(mouse_pos):
                        run = False

            if event.type == pygame.QUIT:
                run = False
                quit_menu = True
        
        chargement(480, HEIGHT-97 , teta, fact)

        
        pygame.display.update()


### _______________MAIN()________________________


def main():
    quit_menu = False
    menu()
    run = True
    clock = pygame.time.Clock()
    dt = 0.7
    
    
    #----------------###  STARS   ###------------------

    star_1 = Star(
        name="Sun",
        mass=1.989e28,  # kg
        radius= 8,
        color=WHITE,  
        position=np.array([-1.496e8, 0], dtype=np.float64), 
        velocity=np.array([0, -297800], dtype=np.float64),  
        trace_val=False
    )
    star_2 = Star(
        name="Sirius",
        mass=1.989e28,  # kg
        radius= 8,
        color=WHITE,  
        position=np.array([1.496e8, 0],dtype=np.float64),  
        velocity=np.array([0, 297800],dtype=np.float64),  
        trace_val=False
    )

    star_3 = Star(
        name="Sirius2",
        mass=1.989e26,  
        radius= 7,
        color=BLUE,  
        position=np.array([-1e8, 2.5e8],dtype=np.float64),  
        velocity=np.array([-47000, -1000],dtype=np.float64),  
        trace_val=False
    )

    star_4 = Star(
        name="Sirius2",
        mass=1.989e26,  
        radius= 7,
        color=RED,  
        position=np.array([1e8, -2.5e8],dtype=np.float64),  
        velocity=np.array([47000, 1000],dtype=np.float64),  
        trace_val=False
    )

    star_system = [star_1, star_2, star_3, star_4]

#-----------------### LOOP ###------------------

    while run:
        clock.tick(800) 
        win.fill(BLACK) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if quit_menu:
            run = False

        for star in star_system:
            star.new_position(dt, star_system)
            star.draw(win)
        pygame.display.update()

    pygame.quit()

main()