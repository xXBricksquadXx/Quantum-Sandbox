import unittest
import sys
import os
import numpy as np

# Ensure root path is accessible
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core_physics.wave_mechanics import QuantumState
from core_physics.bell_test import calculate_correlation
from core_physics.operators import QuantumOperator

class TestQuantumCore(unittest.TestCase):
    
    def test_normalization(self):
        """
        Ensures that the Wavefunction always sums to 1 (Conservation of Probability).
        If this fails, the 'Sandbox' is leaking reality.
        """
        # Create a state with unnormalized inputs (3, 4) -> should normalize to 0.6 and 0.8
        state = QuantumState(3, 4) 
        probs = state.get_probabilities()
        self.assertAlmostEqual(np.sum(probs), 1.0, places=5)
        print(f"✅ Normalization Conserved: {np.sum(probs)}")

    def test_bell_correlation_logic(self):
        """
        Tests the math of the correlation function (The Mirror Link).
        In a perfect 'Mirror' (Entanglement), 00 and 11 should dominate.
        """
        perfect_entanglement = {'00': 500, '11': 500}
        corr = calculate_correlation(perfect_entanglement)
        
        # Correlation should be 1.0 for perfect agreement
        self.assertEqual(corr, 1.0)
        print(f"✅ Bell Logic Verified (Perfect Link): {corr}")

    def test_classical_noise(self):
        """
        Tests random noise. Correlation should be near 0.
        """
        noise = {'00': 250, '11': 250, '01': 250, '10': 250}
        corr = calculate_correlation(noise)
        self.assertEqual(corr, 0.0)
        print(f"✅ Noise Rejection Verified: {corr}")

    def test_operator_integrity(self):
        """
        Ensures the 'Receiver' only accepts Hermitian matrices (Valid Observables).
        If we try to use a scrambled matrix, the system should throw a ValueError.
        """
        valid_matrix = [[1, 0], [0, -1]] # Sigma Z (Hermitian)
        invalid_matrix = [[1, 5], [0, 1]] # Non-Hermitian (Not its own mirror)
        
        # This should pass
        op = QuantumOperator(valid_matrix, "ValidOp")
        self.assertEqual(op.name, "ValidOp")
        
        # This should raise the ValueError (Security Check)
        with self.assertRaises(ValueError):
            QuantumOperator(invalid_matrix, "BadOp")
        print("✅ Operator Integrity Guardrail Active.")

if __name__ == "__main__":
    unittest.main()