import numpy as np
from scipy.linalg import expm

# Stato iniziale (2 livelli, esempio qubit)
psi0 = np.array([1, 0], dtype=complex)

# Hamiltoniana variabile nel tempo (esempio: campi oscillanti)
def H(t):
    omega = 1.0
    delta = 0.5*np.sin(t)
    Ht = np.array([[0, omega], [omega, delta]])
    return Ht

# Evoluzione numerica (passo di tempo dt)
dt = 0.01
T = 10
steps = int(T/dt)
psi = psi0.copy()
t = 0
history = [psi.copy()]
for i in range(steps):
    U = expm(-1j * H(t) * dt)
    psi = U @ psi
    psi = psi / np.linalg.norm(psi)
    history.append(psi.copy())
    t += dt

# Mostra evoluzione stato
print("Evoluzione stato quantistico con Hamiltoniana variabile:")
for i, vec in enumerate(history[::int(steps/10)]):
    print(f"t={i*dt*int(steps/10):.2f}: {vec}")