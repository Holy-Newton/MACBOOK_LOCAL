import numpy as np
import math as m
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600

# Commonly used colors in programming
BLACK = (0, 0, 0)       # Noir
WHITE = (255, 255, 255) # Blanc
RED = (255, 0, 0)       # Rouge
GREEN = (0, 255, 0)     # Vert
BLUE = (0, 0, 255)      # Bleu
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

star_1 = Star(
    name="Sun",
    mass=1.989e30,  # kg
    radius=6.957e8,  # m
    color=WHITE,  # RGB color for the sun
    position=(0, 0),  # Sun is at the center of the solar system
    velocity=(0, 0),  # Sun is stationary in this simulation
    trace_val=False
)
star_2 = Star(
    name="Sirius",
    mass=5.972e24,  # kg
    radius=6.371e6,  # m
    color=WHITE,  # RGB color for Earth
    position=(1.496e11, 0),  # Earth's average distance from the sun in meters
    velocity=(0, 29780),  # Earth's orbital velocity in m/s
    trace_val=False
)

