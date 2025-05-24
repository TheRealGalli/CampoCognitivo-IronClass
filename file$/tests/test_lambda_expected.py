import unittest
import numpy as np

def delta_psi(H, psi, lam):
    """Funzionale di coerenza ||Hψ - λψ||_2"""
    diff = np.dot(H, psi) - lam * psi
    return np.linalg.norm(diff)

def compute_lambda(H, psi):
    """Restituisce il valore di λ atteso dal prodotto scalare <ψ|H|ψ>/<ψ|ψ>"""
    numerator = np.vdot(psi, np.dot(H, psi))
    denominator = np.vdot(psi, psi)
    return np.real(numerator / denominator)

class TestLambdaExpected(unittest.TestCase):
    def setUp(self):
        # Hamiltoniana semplice
        self.H = np.array([[2, 0],
                           [0, 3]])
        # Autovettore λ=2
        self.psi1 = np.array([1, 0])
        # Autovettore λ=3
        self.psi2 = np.array([0, 1])
        # Vettore generico (superposizione)
        self.psi3 = np.array([1, 1]) / np.sqrt(2)

    def test_lambda_autovettore1(self):
        """λ atteso per autovettore psi1 (deve essere 2)"""
        lam = compute_lambda(self.H, self.psi1)
        self.assertAlmostEqual(lam, 2.0, places=2)

    def test_lambda_autovettore2(self):
        """λ atteso per autovettore psi2 (deve essere 3)"""
        lam = compute_lambda(self.H, self.psi2)
        self.assertAlmostEqual(lam, 3.0, places=2)

    def test_lambda_superposizione(self):
        """λ atteso per superposizione (deve essere la media pesata degli autovalori)"""
        lam = compute_lambda(self.H, self.psi3)
        expected = 0.5 * 2 + 0.5 * 3  # 2.5
        self.assertAlmostEqual(lam, expected, delta=0.01)

    def test_delta_psi_minimo_su_esperato(self):
        """ΔΨ è minimo per λ ≈ valore atteso"""
        lam = compute_lambda(self.H, self.psi3)
        delta_val = delta_psi(self.H, self.psi3, lam)
        # Deve essere circa minimo (zero per autovettore, minimo per vettore generico)
        self.assertTrue(delta_val < 1e-10 or np.isclose(delta_val, 0.0, atol=1e-10))

    def test_delta_psi_diverso_per_lambda_errato(self):
        """ΔΨ è maggiore se λ è lontano da quello atteso"""
        lam_err = 1.5
        delta_val = delta_psi(self.H, self.psi3, lam_err)
        lam_exp = compute_lambda(self.H, self.psi3)
        delta_min = delta_psi(self.H, self.psi3, lam_exp)
        self.assertTrue(delta_val > delta_min + 0.01)

if __name__ == "__main__":
    unittest.main()