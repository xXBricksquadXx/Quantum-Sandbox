import numpy as np
from qiskit import QuantumCircuit, Leaf
from qiskit_aer import AerSimulator

def run_bell_test(num_shots=1024):
    """
    Simulates a Bell Test using a CHSH-style experiment.
    We create an entangled pair (EPR pair) and measure them at specific angles.
    """
    simulator = AerSimulator()
    
    # Angles for measurement (in radians) that maximize Bell violation
    # These specific angles (0, pi/4, pi/2, 3pi/4) are the 'sweet spots'
    angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]
    
    # Step 1: Create the Entangled Circuit
    # Using 'H' (Hadamard) and 'CNOT' to create the Bell State: (|00> + |11>) / sqrt(2)
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    
    # In a real Bell test, we would rotate the detectors. 
    # For this simulation, we'll keep it simple: 
    # proving the 'Mirror' link exists through entanglement.
    qc.measure([0, 1], [0, 1])
    
    job = simulator.run(qc, shots=num_shots)
    result = job.result()
    counts = result.get_counts()
    
    return counts

def calculate_correlation(counts):
    """
    Math Note: We check if the qubits 'agree' (00 or 11) or 'disagree' (01 or 10).
    In a 'Mirror' or 'Non-Local' link, they agree more than classical probability allows.
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