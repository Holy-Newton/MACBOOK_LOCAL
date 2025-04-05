import numpy as np
import math as m
import pygame

pygame.init()
WIDTH, HEIGHT = 1200, 900
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitational Trajectory Simulation by Holly Newton")


#constants
dt = 3600
G = 6.67430e-9
# Commonly used colors in programming
BLACK = (0, 0, 0)       # Noir
WHITE = (255, 255, 255) # Blanc
RED = (255, 0, 0)       # Rouge
GREEN = (0, 255, 0)     # Vert
BLUE = (150, 150, 255)      # Bleu
YELLOW = (255, 255, 0)  # Jaune
CYAN = (0, 255, 255)    # Cyan

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
        a = G * other.mass * (other.position - self.position) / r**3
        return a
    
    def new_position(self, dt, star_system):
        OTHERS = star_system.copy()
        OTHERS.remove(self)
        a_tot = np.array([0, 0], dtype=np.float64)
        for other in OTHERS:
            a_tot += self.acceleration(other)
        self.velocity += a_tot * dt
        self.position += self.velocity * dt
        print(self.position)
        

def main():
    run = True
    clock = pygame.time.Clock()
    dt = 1
    
    #----------------###  STARS   ###------------------

    star_1 = Star(
        name="Sun",
        mass=1.989e28,  # kg
        radius= 8,
        color=WHITE,  # RGB color for the sun
        position=np.array([-1.496e8, 0], dtype=np.float64),  # Sun is at the center of the solar system
        velocity=np.array([0, -297800], dtype=np.float64),  # Sun is stationary in this simulation
        trace_val=False
    )
    star_2 = Star(
        name="Sirius",
        mass=1.989e28,  # kg
        radius= 8,
        color=WHITE,  # RGB color for Earth
        position=np.array([1.496e8, 0],dtype=np.float64),  # Earth's average distance from the sun in meters
        velocity=np.array([0, 297800],dtype=np.float64),  # Earth's orbital velocity in m/s
        trace_val=False
    )

    star_3 = Star(
        name="Sirius2",
        mass=1.989e26,  # kg
        radius= 7,
        color=BLUE,  # RGB color for Earth
        position=np.array([-1e8, 2.5e8],dtype=np.float64),  # Earth's average distance from the sun in meters
        velocity=np.array([-31000, -15000],dtype=np.float64),  # Earth's orbital velocity in m/s
        trace_val=False
    )

    star_system = [star_1, star_2, star_3]

#-----------------### LOOP ###------------------

    while run:
        clock.tick(1200) 
        win.fill(BLACK) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for star in star_system:
            star.new_position(dt, star_system)
            star.draw(win)
        pygame.display.update()

    pygame.quit()

main()