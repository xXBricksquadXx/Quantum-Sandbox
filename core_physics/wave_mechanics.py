import numpy as np

class QuantumState:
    """
    A class to represent a simple 2-level quantum system (Qubit).
    Direct implementation of State Vectors and Probability Densities.
    """
    def __init__(self, alpha, beta):
        # Normalize: |alpha|^2 + |beta|^2 must = 1
        norm = np.sqrt(abs(alpha)**2 + abs(beta)**2)
        self.state = np.array([alpha/norm, beta/norm])

    def get_probabilities(self):
        """
        The Born Rule: P(i) = |<i|psi>|^2
        This is the mathematical bridge to the 'Observer Effect'.
        """
        return np.abs(self.state)**2

    def __repr__(self):
        return f"State: {self.state[0]:.3f}|0> + {self.state[1]:.3f}|1>"

# Learning Note: 
# The 'Born Rule' is the specific point where the 'woo' often enters. 
# In standard physics, it's just a probability calculation.