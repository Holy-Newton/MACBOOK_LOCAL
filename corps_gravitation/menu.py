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


def crant_bar( win, mouse_pos, click, x, y, choices, default,length, width, color):  ## Selection bar
    if not hasattr(crant_bar, "val"):
        crant_bar.val = default*length/(choices)
    init = pygame.Rect(x, y, length, width)
    pygame.draw.rect(win, color, init, border_radius=2)

    init_black = pygame.Rect(x+crant_bar.val+4, y+4, length-crant_bar.val-8, width-8)
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

def chargement(win,x , y, teta, fact):
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
    pygame.draw.circle(win, rgb(n), (x,y), 10)
    pygame.draw.circle(win, rgb(n), (x1,y1), 10)

def rgb(n):
    t = 2 * np.pi * n / 255
    r = int((np.sin(t) * 127) + 128)
    g = int((np.sin(t + 2*np.pi/3) * 127) + 128)
    b = int((np.sin(t + 4*np.pi/3) * 127) + 128)
    return (r, g, b)    

def menu(win, WIDTH, HEIGHT):
    
    clock = pygame.time.Clock()
    run = True
    WB, HB = 500,100
    teta = 0.1
    fact = 1
    while run:
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()


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
        text = font.render("==Gravitational Trajectory Simulation====@Holy-Newton==", 1, TRON)
        win.blit(text, (WIDTH/2 - text.get_width()/2, 130 - text.get_height()/1))

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
                draw_text(win, "Start Simulation", 20, (250, HEIGHT-100), TRON)
                draw_text(win, "Start Simulation", 29, (250, HEIGHT-100), TRON)
                WB, HB = 485,85
        else:
            draw_text(win, "Start Simulation", 35, (250, HEIGHT-100), TRON)
            WB, HB = 500,100
        

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  #gauche
                    if start_but.collidepoint(mouse_pos):
                        run = False

            if event.type == pygame.QUIT:
                run = False
                
        
        chargement(win, 489, HEIGHT-97 , teta, fact)

        print(crant_bar(win, mouse_pos, click, WIDTH- 250, 250, 3,1, 200, 20, WHITE))


        
        pygame.display.update()
