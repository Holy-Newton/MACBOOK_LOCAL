import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy.linalg import solve
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
    produit_scalaire = np.dot (V1/norm_V1, V2/norm_V2)
    np.clip(produit_scalaire, -1.0, 1.0)
    angle = np.arccos(produit_scalaire)
    return angle

def symetrie_angle(V, U):
    projection = np.dot(V,U) / np.dot(U,U) * U
    symetrie = (2* projection - V) / np.linalg.norm(2* projection-V)
    return symetrie
''' Creation de la représentation vectorielle d'un rayon lumineux'''








class Ray:
    def __init__(self, position, direction, amplitude=1, phase=0, frequency=1):
        self.position = np.array(position)  # Position vector
        self.direction = np.array(direction)  # Direction vector
        self.amplitude = amplitude  # Amplitude
        self.phase = phase  # Phase
        self.frequency = frequency

    def collision(self, mirror):
        # Calculate the intersection of the ray with the mirror if it exists
        mirror_direction = np.array([np.cos(mirror.gama), np.sin(mirror.gama)])
        a = mirror.position - mirror.length * mirror_direction/2
        b = mirror.position + mirror.length * mirror_direction/2

        ray_start = self.position
        ray_direction = self.direction
        mirror_segment = b - a

        M = np.array([[-ray_direction[0], mirror_segment[0]],
                    [-ray_direction[1], mirror_segment[1]]])
        B = a - ray_start

        try:
            coef, u = solve(M, B)
            if coef >= 0 and 0 <= u <= 1:
                intersection_point = ray_start + coef * ray_direction
                print(f"Intersection found at: {intersection_point}")
                return intersection_point
            else:
                print("No valid intersection found.")
                return False
        except np.linalg.LinAlgError:
            print("LinAlgError, no intersection.")
            return False


    def draw_ray(self, ax, mirror):
        collision = self.collision(mirror)
        if collision:
            intersection = collision
            ax.plot(self.position, intersection, 'ro', label='Intersection')
        else:
            print("yeah, no intersection buddy..")
            end_pos = self.position + self.direction *100
            ax.plot([self.position[0], end_pos[0]], [self.position[1], end_pos[1]], color='blue', lw=2)
        ax.grid()
        ax.legend()
        
    

    def reflect(self, mirror):
        #calcul de la réflextion par rapport à la normale du miroir
        gama = mirror.gama + np.pi/2  # Normale
        direction = self.direction
        angle = angle(gama, direction)
        if angle < np.pi/2:
            # Ray is incident on the mirror
            reflected_direction = direction - 2 * np.dot(direction, gama) * gama
            reflected_ray = Ray(self.position, reflected_direction, self.amplitude * mirror.reflection, self.phase)
            return reflected_ray
        else:
 
            return None
        






        
class Mirror:

    def __init__(self, position, length=1, gama= (np.pi/2), transmission=0.5):
        self.position = np.array(position)
        self.length = length
        self.gama = gama
        self.transmission = transmission
        self.reflection = 1 - transmission
    
    def draw_mirror(self, ax):
        position =  self.position
        x = [position[0]] - self.length/2 * np.cos(self.gama)
        y = [position[1]] - self.length/2 * np.sin(self.gama)
        x_end = [position[0]] + self.length/2 * np.cos(self.gama)
        y_end = [position[1]] + self.length/2 * np.sin(self.gama)
        ax.plot([x[0], x_end[0]], [y[0], y_end[0]], color='red', lw=2, label='Mirror')







### MIRRORS

mirror1 = Mirror(position=[50, 50], length=50, gama=0, transmission=0)

### RAYS
rayon = Ray(position=[2, 0], direction=[1, 1], amplitude=1, phase=0, frequency=1)

Ensemble_miroirs = { mirror1 }
for mirror in Ensemble_miroirs:
    mirror.draw_mirror(ax)
    rayon.draw_ray(ax, mirror)


# Plot settings and initialization

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Fabry-Perot Interferometer Simulation')

plt.show()
