from sympy import symbols, sin, simplify, Matrix

# Coordinate sferiche: r, theta, phi
r, theta, phi = symbols('r theta phi')
# Metrica sferica 3D (senza tempo)
g = Matrix([
    [1, 0, 0],
    [0, r**2, 0],
    [0, 0, r**2 * sin(theta)**2]
])

# Calcolo delle derivate e simboli di Christoffel (semplificato)
# Usa RicciTensor di SymPy per automatizzare
from sympy.diffgeom import Manifold, Patch, CoordSystem, metric_to_Christoffel_2nd, metric_to_Ricci_components

m = Manifold('M', 3)
patch = Patch('P', m)
coords = CoordSystem('sph', patch, ['r', 'theta', 'phi'])
metric = {(0,0):1, (1,1):r**2, (2,2):r**2*sin(theta)**2}

Ricci = metric_to_Ricci_components(metric, coords)
print("Tensore di Ricci per la metrica sferica:")
for idx, val in Ricci.items():
    print(f"Ricci[{idx}] =", simplify(val))