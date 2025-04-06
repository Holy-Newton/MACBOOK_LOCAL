import numpy as np
import math as m
import pygame

# CONSTANT

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
    

def menu(win, WIDTH, HEIGHT):
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
