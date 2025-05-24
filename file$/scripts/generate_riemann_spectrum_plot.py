import numpy as np
import matplotlib.pyplot as plt

# Zeri non banali della zeta di Riemann (prime 20 parti immaginarie note)
riemann_zeros_im = [
    14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
    37.586178, 40.918719, 43.327073, 48.005150, 49.773832,
    52.970321, 56.446247, 59.347044, 60.831780, 65.112544,
    67.079811, 69.546402, 72.067158, 75.704690, 77.144840
]

zeros = np.array(riemann_zeros_im)

fig, ax = plt.subplots(figsize=(6, 8), dpi=120)
ax.vlines(zeros, 0, 1, color='navy', lw=2)
ax.set_ylim(0, 1)
ax.set_xlim(0, zeros[-1] + 5)
ax.set_xlabel(r'$\mathrm{Im}(s)$', fontsize=14)
ax.set_yticks([])
ax.set_title("First 20 Riemann Zeta Zeros (Critical Line)", fontsize=15)
ax.grid(axis='x', linestyle='--', alpha=0.4)

plt.tight_layout()
plt.savefig("docs/riemann_spectrum_plot.png")
plt.close()