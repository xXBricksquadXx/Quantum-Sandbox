import numpy as np
from core_physics.operators import QuantumOperator

class LadderOperator(QuantumOperator):
    """The 'Gain Control'. Moves energy up/down the rungs."""
    def __init__(self, dimension, kind='annihilation'):
        matrix = np.zeros((dimension, dimension))
        for n in range(1, dimension):
            if kind == 'annihilation':
                matrix[n-1, n] = np.sqrt(n)
            else: # creation (a_dagger)
                matrix[n, n-1] = np.sqrt(n)
        
        self.matrix = matrix
        self.name = f"Ladder_{kind}"

    def step(self, state_vector):
        return self.matrix @ state_vector

class HarmonicOscillator:
    """
    The 'Box of Molecules'. 
    Calculates how internal vibration adds to the system's total mass.
    """
    def __init__(self, omega, mass_zero):
        self.omega = omega  # Angular frequency (The 'Vibe')
        self.m0 = mass_zero # Rest mass (The 'Cold Potato')

    def calculate_system_energy(self, n_level):
        """E = (n + 1/2) * hbar * omega"""
        hbar = 1.0 
        return (n_level + 0.5) * hbar * self.omega

    def get_invariant_mass(self, n_level):
        """m = E / c^2"""
        c = 1.0 
        energy = self.calculate_system_energy(n_level)
        return energy / (c**2)