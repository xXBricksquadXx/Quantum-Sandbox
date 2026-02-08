import unittest
import numpy as np
import sys
import os

# Root anchor for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core_physics.neuro_state import NeuroSubsystem

class TestNeuroPurity(unittest.TestCase):
    def test_purity_baseline(self):
        """
        Ensures a fresh state starts as 'Pure' (Purity = 1.0).
        This represents the 'Spacetime Memory' or 'Ideal' state.
        """
        # A simple superposition state
        state = np.array([1, 1]) / np.sqrt(2)
        pfc = NeuroSubsystem(state)
        
        self.assertAlmostEqual(pfc.get_purity(), 1.0, places=5)
        print(f"✅ Baseline Purity Verified: {pfc.get_purity()}")

    def test_error_correction_gain(self):
        """
        Simulates a 'Mixed' (Noisy) state and applies the Phased Array 
        to see if Purity increases.
        """
        # Initial Pure State
        state = np.array([1, 0])
        pfc = NeuroSubsystem(state)
        
        # Manually 'Decohere' the matrix (inject noise/trauma)
        pfc.rho = np.array([[0.6, 0.1], [0.1, 0.4]])
        initial_purity = pfc.get_purity() # Should be < 1.0
        
        # Apply Reference Signal (Pure Spacetime Memory)
        reference = np.outer(state, np.conj(state))
        new_purity = pfc.apply_error_correction(reference)
        
        self.assertGreater(new_purity, initial_purity)
        print(f"✅ Error Correction Verified: {initial_purity:.4f} -> {new_purity:.4f}")

if __name__ == "__main__":
    unittest.main()