import numpy as np

class QuantumOperator:
    """
    Finalized Operator Class. 
    Acts as the 'Receiver' to extract observables from the state array.
    """
    def __init__(self, matrix, name):
        self.matrix = np.array(matrix)
        self.name = name
        # HERMITIAN CHECK: Ensures signal integrity and real-world measurability.
        if not np.allclose(self.matrix, self.matrix.conj().T):
            raise ValueError(f"CRITICAL: {name} is non-Hermitian. Signal scrambled.")

    def observe(self, quantum_state):
        """Calculates the expectation value (The average lab reading)."""
        psi = quantum_state.state
        return np.real(np.vdot(psi, self.matrix @ psi))

# PRE-SET INSTRUMENTATION
# Sigma_Z: Measuring the basic binary state (Matter/Ground)
sigma_z = QuantumOperator([[1, 0], [0, -1]], name="Z-Observable")