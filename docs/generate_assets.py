import os
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from core_physics.harmonic_oscillator import HarmonicOscillator
from core_physics.neuro_state import NeuroSubsystem

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

    # 3. Dirac Vacuum & L-State Energy Chart
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

    # 4. Vibration-Mass Slope (Lecture 5)
    print("📡 Generating Vibration-Mass Slope...")
    box = HarmonicOscillator(omega=2.0, mass_zero=1.0)
    n_levels = np.arange(0, 10)
    masses = [box.get_invariant_mass(n) for n in n_levels]
    plt.figure(figsize=(8, 5))
    plt.plot(n_levels, masses, marker='o', linestyle='-', color='purple', label='m = E/c²')
    plt.title("The Kinetic-Mass Bridge: Energy vs. Invariant Mass")
    plt.xlabel("Vibrational Level (n)")
    plt.ylabel("Total System Mass (Invariant)")
    plt.grid(True, linestyle='--')
    plt.savefig('docs/vibration_mass_slope.png')
    print("✅ Vibration-Mass Slope saved.")

    # 5. NEW: Neuro-Purity Heatmap (Lecture 6 - Subsystems)
    print("🧠 Generating Neuro-Purity Recovery Heatmap...")
    # Create a grid of Noise vs. Correction Strength
    noise_range = np.linspace(0, 1, 10)
    correction_range = np.linspace(0, 1, 10)
    purity_map = np.zeros((10, 10))

    for i, noise in enumerate(noise_range):
        for j, corr in enumerate(correction_range):
            # Base state + noise
            state = np.array([1, 0])
            pfc = NeuroSubsystem(state)
            # Simulate noise by mixing with identity (Maximum entropy)
            pfc.rho = (1-noise) * pfc.rho + (noise) * 0.5 * np.eye(2)
            # Apply correction
            ref = np.outer(state, np.conj(state))
            pfc.rho = (1-corr) * pfc.rho + (corr) * ref
            purity_map[i, j] = pfc.get_purity()

    plt.figure(figsize=(8, 6))
    plt.imshow(purity_map, extent=[0, 1, 0, 1], origin='lower', cmap='plasma')
    plt.colorbar(label='Purity Score [Tr(ρ²)]')
    plt.title("Neuro-Quantum Recovery: Phased Array vs. Noise")
    plt.xlabel("Correction Strength (Phased Array)")
    plt.ylabel("Noise Level (Decoherence)")
    plt.savefig('docs/neuro_purity_recovery.png')
    print("✅ Neuro-Purity Heatmap saved.")
    
    print("\n🔬 All systems coherent. Ready for commit.")

if __name__ == "__main__":
    generate_lab_report()