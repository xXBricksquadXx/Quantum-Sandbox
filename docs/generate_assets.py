import os
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from core_physics.harmonic_oscillator import HarmonicOscillator
from core_physics.neuro_state import NeuroSubsystem
from core_physics.universal_clock import UniversalClock

def generate_lab_report():
    print("🚀 Initializing Lab Asset Generation...")
    if not os.path.exists('docs'): os.makedirs('docs')

    # 1. Bell State Circuit
    qc = QuantumCircuit(2)
    qc.h(0); qc.cx(0, 1)
    qc.draw(output='mpl', filename='docs/bell_state_circuit.png')

    # 2. Manifestation Histogram
    qc_render = QuantumCircuit(1, 1)
    qc_render.ry(0.7 * np.pi, 0); qc_render.measure(0, 0)
    sim = AerSimulator()
    counts = sim.run(qc_render, shots=1024).result().get_counts()
    plot_histogram(counts).savefig('docs/manifestation_probabilities.png')

    # 3. Energy Index Chart
    levels = np.array([-1, 0, 1, 2])
    labels = ['Dirac Sea (-1)', 'Ground (0)', 'L=1 (Hydrogen)', 'L=2 (Hydrogen)']
    plt.figure(figsize=(8, 5))
    plt.hlines(levels, 0, 1, colors=['red', 'black', 'blue', 'green'])
    for i, txt in enumerate(labels): plt.annotate(txt, (1.01, levels[i]))
    plt.savefig('docs/energy_indices.png')

    # 4. Vibration-Mass Slope
    box = HarmonicOscillator(omega=2.0, mass_zero=1.0)
    n = np.arange(0, 10); masses = [box.get_invariant_mass(lvl) for lvl in n]
    plt.figure(); plt.plot(n, masses, 'p-'); plt.savefig('docs/vibration_mass_slope.png')

    # 5. Neuro-Purity Recovery
    noise = np.linspace(0, 1, 10); corr = np.linspace(0, 1, 10)
    p_map = np.zeros((10, 10))
    for i, n_val in enumerate(noise):
        for j, c_val in enumerate(corr):
            pfc = NeuroSubsystem(np.array([1, 0]))
            pfc.rho = (1-n_val)*pfc.rho + n_val*0.5*np.eye(2)
            pfc.rho = (1-c_val)*pfc.rho + c_val*np.outer([1, 0], [1, 0])
            p_map[i, j] = pfc.get_purity()
    plt.figure(); plt.imshow(p_map, cmap='plasma'); plt.savefig('docs/neuro_purity_recovery.png')

    # 6. Chronos Dilation Map
    print("⏳ Generating Relativistic Dilation Map...")
    mass_range = np.linspace(1, 100000, 20)
    v_indices = np.linspace(-1, 1, 20)
    d_map = np.zeros((20, 20))
    for i, m in enumerate(mass_range):
        for j, v in enumerate(v_indices):
            clock = UniversalClock(observer_mass_kg=m, vacuum_index=v)
            d_map[i, j] = clock.calculate_dilation()
    plt.figure(); plt.imshow(d_map, extent=[-1, 1, 1, 100000], aspect='auto', cmap='viridis')
    plt.colorbar(label='Dilation Factor'); plt.savefig('docs/chronos_dilation_map.png')
    
    print("\n🔬 All systems coherent. Ready for commit.")

if __name__ == "__main__":
    generate_lab_report()