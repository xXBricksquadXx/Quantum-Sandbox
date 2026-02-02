import os
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from core_physics.harmonic_oscillator import HarmonicOscillator

def generate_lab_report():
    print("🚀 Initializing Lab Asset Generation...")
    if not os.path.exists('docs'): os.makedirs('docs')

    # 1. Mirror Link (Bell State)
    qc = QuantumCircuit(2)
    qc.h(0); qc.cx(0, 1)
    qc.draw(output='mpl', filename='docs/bell_state_circuit.png')
    print("✅ Bell State Circuit saved.")

    # 2. Reality-Render (Manifestation)
    qc_render = QuantumCircuit(1, 1)
    qc_render.ry(0.7 * np.pi, 0); qc_render.measure(0, 0)
    sim = AerSimulator()
    counts = sim.run(qc_render, shots=1024).result().get_counts()
    plot_histogram(counts).savefig('docs/manifestation_probabilities.png')
    print("✅ Manifestation Histogram saved.")

    # 3. Dirac Vacuum & L-State Energy Chart (Lecture 4)
    levels = np.array([-1, 0, 1, 2])
    labels = ['Dirac Sea (-1)', 'Ground (0)', 'L=1 (Hydrogen)', 'L=2 (Hydrogen)']
    
    plt.figure(figsize=(8, 5))
    plt.hlines(levels, 0, 1, colors=['red', 'black', 'blue', 'green'], linestyles='solid')
    for i, txt in enumerate(labels):
        plt.annotate(txt, (1.01, levels[i]), fontsize=10)
    
    plt.title("Quantum State Array: Energy Indices")
    plt.ylabel("Energy Level (Eigenvalues)")
    plt.xticks([])
    plt.grid(axis='y', linestyle='--')
    plt.savefig('docs/energy_indices.png')
    print("✅ Energy Index Chart saved.")

    # 4. NEW: Vibration-Mass Slope (Lecture 5 - Kinetic Mass Bridge)
    # Proving that internal vibration (omega) increases Invariant Mass
    print("📡 Generating Vibration-Mass Slope...")
    box = HarmonicOscillator(omega=2.0, mass_zero=1.0)
    
    n_levels = np.arange(0, 10)
    masses = [box.get_invariant_mass(n) for n in n_levels]
    
    plt.figure(figsize=(8, 5))
    plt.plot(n_levels, masses, marker='o', linestyle='-', color='purple', label='m = E/c²')
    plt.title("The Kinetic-Mass Bridge: Energy vs. Invariant Mass")
    plt.xlabel("Vibrational Level (n)")
    plt.ylabel("Total System Mass (Invariant)")
    plt.legend()
    plt.grid(True, linestyle='--')
    plt.savefig('docs/vibration_mass_slope.png')
    print("✅ Vibration-Mass Slope saved.")
    
    print("\n🔬 All systems coherent. Ready for commit.")

if __name__ == "__main__":
    generate_lab_report()