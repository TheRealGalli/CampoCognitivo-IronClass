import unittest
import numpy as np

def delta_psi(H, psi, lam):
    """Funzionale di coerenza ||Hψ - λψ||_2"""
    diff = np.dot(H, psi) - lam * psi
    return np.linalg.norm(diff)

class TestDeltaPsiSimulazioniExtra(unittest.TestCase):
    def setUp(self):
        # Hamiltoniana semplice 2x2
        self.H = np.array([[2, 0],
                           [0, 3]])
        # Due autovettori
        self.psi1 = np.array([1, 0])
        self.psi2 = np.array([0, 1])
        # Vettore generico
        self.psi_gen = np.array([1, 1]) / np.sqrt(2)

    def test_picco_coerenza_fora_critica(self):
        """
        Simulazione 1: λ con Re(s) ≠ 0.5 (ad esempio λ=2.7)
        Ci aspettiamo che ΔΨ sia massimo (non nullo) per vettore generico.
        """
        lam = 2.7
        val = delta_psi(self.H, self.psi_gen, lam)
        self.assertGreater(val, 0.0)
        print(f"Simulazione 1 (λ={lam}): ΔΨ = {val:.4f} (vettore generico)")

    def test_picco_coerenza_su_autovettore_fuori_critica(self):
        """
        Simulazione 2: λ con Re(s) ≠ 0.5 su autovettore non corrispondente (λ=2, psi2)
        ΔΨ deve essere massimo, perché psi2 non è autovettore per λ=2.
        """
        lam = 2
        val = delta_psi(self.H, self.psi2, lam)
        self.assertGreater(val, 0.0)
        print(f"Simulazione 2 (λ={lam}, psi2): ΔΨ = {val:.4f}")

if __name__ == "__main__":
    unittest.main()