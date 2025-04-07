import numpy as np

# Définir les couleurs
WHITE = (255, 255, 255)

# Liste des données initiales
init_data = [
    {"position": np.array([-1.496e8, 0], dtype=np.float64), "velocity": np.array([0, -297800], dtype=np.float64), "mass": 1.989e28, "color": WHITE},
    {"position": np.array([1.496e8, 0], dtype=np.float64), "velocity": np.array([0, 297800], dtype=np.float64), "mass": 1.989e28, "color": WHITE},
    {"position": np.array([1e8, -2.5e8], dtype=np.float64), "velocity": np.array([-47000, -1000], dtype=np.float64), "mass": 1.989e26, "color": WHITE},
    {"position": np.array([-1.496e8, 0], dtype=np.float64), "velocity": np.array([47000, 1000], dtype=np.float64), "mass": 1.989e26, "color": WHITE},
]

# Définir la classe Star
class Star:
    def __init__(self, position, velocity, mass, color):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.color = color

# Créer les instances de Star
stars = []
for data in init_data:
    star = Star(
        position=data["position"],
        velocity=data["velocity"],
        mass=data["mass"],
        color=data["color"]
    )
    stars.append(star)

# Utiliser les instances
for star in stars:
    print(f"Position: {star.position}, Velocity: {star.velocity}, Mass: {star.mass}, Color: {star.color}")
    