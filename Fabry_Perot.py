import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, odeint
import sympy as sp

'''
Fabry-Perot Interferometer Simulation
This code simulates the behavior of a Fabry-Perot interferometer, which consists of two parallel mirrors
 separated by a distance L. The simulation calculates the interference pattern based on the wavelength of light and the distance between the mirrors.
 With the ability to visualize the interference pattern and the phase difference between the light waves reflected from the mirrors.'''


fig, ax = plt.subplots(1, 1, figsize=(6,6))


def angle(V1, V2):
    norm_V1 = np.linalg.norm(V1)
    norm_V2 = np.linalg.norm(V2)
    produit_scalaire = np.dot (norm_V1, norm_V2)
    angle = np.arcos(produit_scalaire)
    return angle

''' Creation de la représentation vectorielle d'un rayon lumineux'''
class Ray:
    def __init__(self, position, direction, amplitude=1, phase=0, frequency=1):
        self.position = np.array(position)  # Position vector
        self.direction = np.array(direction)  # Direction vector
        self.amplitude = amplitude  # Amplitude
        self.phase = phase  # Phase
        self.frequency = frequency

    def draw_ray(self, ax):
        end_pos = self.position + self.direction *100
        ax.plot([self.position[0], end_pos[0]], [self.position[1], end_pos[1]], color='blue', lw=2)
        ax.grid()
        ax.legend()
        
    def collision(self, mirror):

    def reflect(self, mirror):
        #calcul de la réflextion par rapport à la normale du miroir
        normal = mirror.normal
        direction = self.direction
        angle = angle(normal, direction)
        if angle < np.pi/2:
            # Ray is incident on the mirror
            reflected_direction = direction - 2 * np.dot(direction, normal) * normal
            reflected_ray = Ray(self.position, reflected_direction, self.amplitude * mirror.reflection, self.phase)
            return reflected_ray
        else:
            # Ray is not incident on the mirror
            return None

class Mirror:
    def __init__(self, position, length=1, normal= (np.pi/2), transmission=0.5):
        self.position = np.array(position)
        self.length = length
        self.normal = normal
        self.transmission = transmission
        self.reflection = 1 - transmission
    
    def draw_mirror(self, ax):
        position =  self.position
        x = [position[0]] - self.length/2 * np.cos(self.normal)
        y = [position[1]] - self.length/2 * np.sin(self.normal)
        x_end = [position[0]] + self.length/2 * np.cos(self.normal)
        y_end = [position[1]] + self.length/2 * np.sin(self.normal)
        ax.plot([x[0], x_end[0]], [y[0], y_end[0]], color='red', lw=2, label='Mirror')




mirror1 = Mirror(position=[50, 50], length=50, normal=0, transmission=0)
mirror1.draw_mirror(ax)

rayon = Ray(position=[0, 0], direction=[1, 1], amplitude=1, phase=0, frequency=1)
rayon.draw_ray(ax)

plt.show()
