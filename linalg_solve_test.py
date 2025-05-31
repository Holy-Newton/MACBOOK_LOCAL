import numpy as np
from scipy.linalg import solve

A = np.array([[2,1],
              [1,3]])
b = np.array([8,13])
x = solve(A,b)

print("la solution x et y:", x)


'''symetrie d'un vecteur par rapport à un autre vecteur'''
'''
import numpy as np
import matplotlib.pyplot as plt

# Vecteurs
v = np.array([2, 3])
u = np.array([1, 0.5])  # vecteur directeur

# Projection de v sur u
proj_v_on_u = (np.dot(v, u) / np.dot(u, u)) * u

# Symétrique
v_sym = 2 * proj_v_on_u - v

# Tracé
origin = np.array([0, 0])
plt.quiver(*origin, *v, color='blue', angles='xy', scale_units='xy', scale=1, label='v')
plt.quiver(*origin, *u, color='green', angles='xy', scale_units='xy', scale=1, label='u')
plt.quiver(*origin, *v_sym, color='red', angles='xy', scale_units='xy', scale=1, label='sym(v)')

# Affichage
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
'''