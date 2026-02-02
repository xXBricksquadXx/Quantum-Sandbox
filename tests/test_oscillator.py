import unittest
import sys
import os

# Ensure the root directory is in the path so it can find 'core_physics'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core_physics.harmonic_oscillator import HarmonicOscillator

class TestOscillator(unittest.TestCase):
    def test_mass_energy_increase(self):
        """Ensures that a 'Hot' box (higher n) weighs more than a 'Cold' box."""
        box = HarmonicOscillator(omega=2.0, mass_zero=1.0)
        
        mass_ground = box.get_invariant_mass(n_level=0)
        mass_excited = box.get_invariant_mass(n_level=5)
        
        self.assertTrue(mass_excited > mass_ground)
        print(f"✅ Mass Increase Verified: {mass_ground} -> {mass_excited}")

if __name__ == "__main__":
    unittest.main()