import os
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator

def generate_lab_report():
    print("🚀 Initializing Lab Asset Generation...")
    
    # Ensure docs directory exists
    if not os.path.exists('docs'):
        os.makedirs('docs')

    # 1. Generate the 'Mirror Link' (Bell State) Circuit
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.draw(output='mpl', filename='docs/bell_state_circuit.png')
    print("✅ Bell State Circuit saved to docs/")

    # 2. Run a Reality-Render Histogram
    # We'll simulate 1024 'manifestation' attempts at 70% intention
    qc_render = QuantumCircuit(1, 1)
    qc_render.ry(0.7 * 3.14159, 0)
    qc_render.measure(0, 0)
    
    sim = AerSimulator()
    counts = sim.run(qc_render, shots=1024).result().get_counts()
    
    fig = plot_histogram(counts)
    fig.savefig('docs/manifestation_probabilities.png')
    print("✅ Manifestation Histogram saved to docs/")
    print("\n🔬 All systems coherent. Ready for commit.")

if __name__ == "__main__":
    generate_lab_report()