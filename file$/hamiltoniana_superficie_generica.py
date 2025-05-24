from sympy import symbols, Matrix, diff, simplify, Function

# Coordinate generiche su superficie (u, v) e tempo t
u, v, t, m = symbols('u v t m')
psi = Function('psi')(u, v, t)

# Metrica generica g_ij (2x2)
g11 = Function('g11')(u, v)
g12 = Function('g12')(u, v)
g22 = Function('g22')(u, v)
g = Matrix([[g11, g12], [g12, g22]])
g_inv = simplify(g.inv())
sqrtg = simplify((g.det())**0.5)

# Operatore Laplace-Beltrami (in 2D)
def laplace_beltrami(f):
    term1 = diff(sqrtg * g_inv[0,0] * diff(f, u), u)
    term2 = diff(sqrtg * g_inv[0,1] * diff(f, v), u)
    term3 = diff(sqrtg * g_inv[1,0] * diff(f, u), v)
    term4 = diff(sqrtg * g_inv[1,1] * diff(f, v), v)
    return (1/sqrtg) * (term1 + term2 + term3 + term4)

# Hamiltoniana quantistica (operatore energia)
def hamiltonian(f):
    return - (1/(2*m)) * laplace_beltrami(f)

# Esempio: psi(u,v)
Hpsi = hamiltonian(psi)
print("Hamiltoniana per una particella su superficie generica (simbolico):")
print(Hpsi)