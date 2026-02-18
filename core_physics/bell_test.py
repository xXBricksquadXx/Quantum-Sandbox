import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def run_bell_test(num_shots=1024):
    """
    Simulates a Bell Pair measurement to verify Entanglement Correlation.
    
    NOTE: This specific function runs a standard basis measurement (Z-basis).
    It verifies that the qubits are "Mirrored" (Perfectly Correlated).
    
    To prove 'Non-Locality' (CHSH Violation), we would rotate the bases 
    by the 'Sweet Spot' angles: [0, pi/4, pi/2, 3pi/4].
    For this module, we focus on establishing the link (Correlation = 1.0).
    """
    simulator = AerSimulator()
    
    # Step 1: Create the Entangled Circuit (The Bell State)
    # Using 'H' (Hadamard) and 'CNOT' to create: (|00> + |11>) / sqrt(2)
    qc = QuantumCircuit(2, 2)
    qc.h(0)       # Put q0 into Superposition
    qc.cx(0, 1)   # Entangle q1 with q0
    
    # Step 2: Measure in the Standard Basis
    # If the link is real, q0 and q1 will always match (00 or 11).
    qc.measure([0, 1], [0, 1])
    
    job = simulator.run(qc, shots=num_shots)
    result = job.result()
    counts = result.get_counts()
    
    return counts

def calculate_correlation(counts):
    """
    Calculates the Correlation Coefficient.
    
    Logic:
    - Agreements (00, 11): The qubits 'mirrored' each other.
    - Disagreements (01, 10): The link failed (Noise/Decoherence).
    
    Returns:
    - 1.0: Perfect Entanglement (The Mirror Link)
    - 0.0: No Link (Random Noise)
    """
    total = sum(counts.values())
    agreements = counts.get('00', 0) + counts.get('11', 0)
    disagreements = counts.get('01', 0) + counts.get('10', 0)
    
    correlation = (agreements - disagreements) / total
    return correlation

if __name__ == "__main__":
    results = run_bell_test()
    print(f"Experimental Counts: {results}")
    print(f"Correlation Coefficient: {calculate_correlation(results)}")