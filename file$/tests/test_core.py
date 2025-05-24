import unittest
import numpy as np

# Esempio di funzione di coerenza (da core pubblico)
def delta_psi(H, psi, lam):
    """Calcola il funzionale di coerenza ||Hψ - λψ||_2"""
    diff = np.dot(H, psi) - lam * psi
    return np.linalg.norm(diff)

class TestCoreCoerenza(unittest.TestCase):
    def setUp(self):
        # Matrice Hamiltoniana semplice (2x2)
        self.H = np.array([[2, 0],
                           [0, 3]])
        # Autovettori normali
        self.psi1 = np.array([1, 0])
        self.psi2 = np.array([0, 1])
        # Vettore generico (non autovettore)
        self.psi3 = np.array([1, 1]) / np.sqrt(2)

    def test_coerenza_autovettore_1(self):
        """Test: coerenza nulla per autovettore λ=2"""
        val = delta_psi(self.H, self.psi1, 2)
        self.assertAlmostEqual(val, 0.0, places=12)

    def test_coerenza_autovettore_2(self):
        """Test: coerenza nulla per autovettore λ=3"""
        val = delta_psi(self.H, self.psi2, 3)
        self.assertAlmostEqual(val, 0.0, places=12)

    def test_non_autovettore(self):
        """Test: coerenza positiva per vettore non autovettore"""
        val = delta_psi(self.H, self.psi3, 2)
        self.assertGreater(val, 0.0)

if __name__ == "__main__":
    unittest.main()