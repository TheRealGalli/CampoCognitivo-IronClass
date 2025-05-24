import numpy as np

# Stato misto (matrice densità)
rho = np.array([[0.7, 0.2],
                [0.2, 0.3]])

# Coerenza quantistica (l1-norm)
def quant_coherence(rho):
    d = rho.shape[0]
    coh = 0
    for i in range(d):
        for j in range(d):
            if i != j:
                coh += np.abs(rho[i,j])
    return coh

print("Matrice densità:")
print(rho)
print("Coerenza quantistica (l1-norm):", quant_coherence(rho))