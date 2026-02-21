import os
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from core_physics.harmonic_oscillator import HarmonicOscillator
from core_physics.neuro_state import NeuroSubsystem
from core_physics.universal_clock import UniversalClock
from core_physics.auditor_logic import AuditorLogic

def generate_lab_report():
    print("🚀 Initializing Lab Asset Generation (IBM Style Standard)...")
    if not os.path.exists('docs'): os.makedirs('docs')

    # 1. Bell State Circuit
    # ---------------------------------------------------------
    qc = QuantumCircuit(2)
    qc.h(0); qc.cx(0, 1)
    qc.draw(output='mpl', filename='docs/bell_state_circuit.png')
    print("✅ Bell State Circuit saved.")

    # 2. Manifestation Histogram
    # ---------------------------------------------------------
    qc_render = QuantumCircuit(1, 1)
    qc_render.ry(0.7 * np.pi, 0); qc_render.measure(0, 0)
    sim = AerSimulator()
    counts = sim.run(qc_render, shots=1024).result().get_counts()
    plot_histogram(counts, title="Manifestation Probability (State Collapse)").savefig('docs/manifestation_probabilities.png')
    print("✅ Manifestation Histogram saved.")

    # 3. Energy Index Chart
    # ---------------------------------------------------------
    levels = np.array([-1, 0, 1, 2])
    labels = ['Dirac Sea (-1)', 'Ground (0)', 'L=1 (Hydrogen)', 'L=2 (Hydrogen)']
    plt.figure(figsize=(10, 6))
    plt.hlines(levels, 0, 1, colors=['red', 'black', 'blue', 'green'], linewidth=2)
    for i, txt in enumerate(labels): 
        plt.annotate(txt, (1.02, levels[i]), fontsize=12, verticalalignment='center')
    plt.title("Quantum State Array: Global Energy Indices", fontsize=14, fontweight='bold')
    plt.ylabel("Energy Eigenvalues (n)", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('docs/energy_indices.png')
    print("✅ Energy Index Chart saved.")

    # 4. Vibration-Mass Slope
    # ---------------------------------------------------------
    box = HarmonicOscillator(omega=2.0, mass_zero=1.0)
    n = np.arange(0, 10)
    masses = [box.get_invariant_mass(lvl) for lvl in n]
    plt.figure(figsize=(10, 6))
    plt.plot(n, masses, 'o-', color='#800080', linewidth=2, markersize=8, label=r'$m = E/c^2$')
    plt.title("The Kinetic-Mass Bridge: Vibration vs. Invariant Mass", fontsize=14, fontweight='bold')
    plt.xlabel("Vibrational Level (n)", fontsize=12)
    plt.ylabel(r"Invariant Mass ($E/c^2$)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig('docs/vibration_mass_slope.png')
    print("✅ Vibration-Mass Slope saved.")

    # 5. Neuro-Purity Recovery Heatmap
    # ---------------------------------------------------------
    noise = np.linspace(0, 1, 10)
    corr = np.linspace(0, 1, 10)
    p_map = np.zeros((10, 10))
    for i, n_val in enumerate(noise):
        for j, c_val in enumerate(corr):
            pfc = NeuroSubsystem(np.array([1, 0]))
            pfc.rho = (1-n_val)*pfc.rho + n_val*0.5*np.eye(2)
            pfc.rho = (1-c_val)*pfc.rho + c_val*np.outer([1, 0], [1, 0])
            p_map[i, j] = pfc.get_purity()
    plt.figure(figsize=(10, 8))
    plt.imshow(p_map, extent=[0, 1, 0, 1], origin='lower', cmap='plasma', aspect='auto')
    plt.colorbar(label=r'Purity Score [$Tr(\rho^2)$]')
    plt.title("Neuro-Quantum Recovery: Phased Array Efficiency", fontsize=14, fontweight='bold')
    plt.xlabel("Correction Strength (Phased Array Intensity)", fontsize=12)
    plt.ylabel("Noise Level (Environmental Decoherence)", fontsize=12)
    plt.tight_layout()
    plt.savefig('docs/neuro_purity_recovery.png')
    print("✅ Neuro-Purity Heatmap saved.")

    # 6. Chronos Dilation Map
    # ---------------------------------------------------------
    mass_range = np.linspace(1, 100000, 20)
    v_indices = np.linspace(-1, 1, 20)
    d_map = np.zeros((20, 20))
    for i, m in enumerate(mass_range):
        for j, v in enumerate(v_indices):
            clock = UniversalClock(observer_mass_kg=m, vacuum_index=v)
            d_map[i, j] = clock.calculate_dilation()
    plt.figure(figsize=(10, 8))
    plt.imshow(d_map, extent=[-1, 1, 1, 100000], aspect='auto', origin='lower', cmap='viridis')
    plt.colorbar(label=r'Dilation Factor ($t_{obs} / t_{univ}$)')
    plt.title("Project Chronos: Relativistic Time Dilation", fontsize=14, fontweight='bold')
    plt.xlabel("Vacuum Index (Negative = Warp | Positive = Gravity)", fontsize=12)
    plt.ylabel("Observer Mass (kg)", fontsize=12)
    plt.tight_layout()
    plt.savefig('docs/chronos_dilation_map.png')
    print("✅ Chronos Dilation Map saved.")

    # 7. Light Cone & Wormhole Topology
    # ---------------------------------------------------------
    x = np.linspace(-15, 15, 100)
    plt.figure(figsize=(10, 10))
    plt.fill_between(x, np.abs(x), 15, color='#d3d3d3', alpha=0.4, label='Causal Future')
    plt.plot(10, 5, 'ro', markersize=12, label='Event in ELSEWHERE')
    plt.plot(0, 0, 'bo', markersize=12, label='Observer (Now)')
    plt.annotate('', xy=(10, 5), xytext=(0, 0), arrowprops=dict(arrowstyle='<->', color='#32CD32', lw=3, linestyle='--'))
    plt.title("Relativistic Causality: The Wormhole Bypass", fontsize=16, fontweight='bold')
    plt.xlabel("Space (Light Years)"); plt.ylabel("Time (Years)")
    plt.legend(loc='upper left')
    plt.xlim(-12, 12); plt.ylim(0, 12)
    plt.tight_layout()
    plt.savefig('docs/light_cone_bypass.png')
    print("✅ Light Cone Bypass Graph saved.")

    # 8. NEW: Auditor Logic - Intent Purity vs. Market Time
    # ---------------------------------------------------------
    print("⏳ Generating Auditor State-Sync Map...")
    auditor = AuditorLogic(observer_mass=80, vacuum_index=-1)
    time_steps = np.arange(0, 50)
    purities = []
    
    # Simulate a stream of intent with fluctuating environmental noise
    for t in time_steps:
        # Intent fluctuates but maintains a core "Spirit" signal
        sim_intent = "Synchronizing Universe..." if t % 5 == 0 else "Background Noise"
        result = auditor.process_intent_state(sim_intent)
        purities.append(result["purity_score"])

    plt.figure(figsize=(12, 6))
    plt.plot(time_steps, purities, color='#00FFFF', linewidth=2.5, label='Auditor Purity')
    plt.axhline(y=0.85, color='r', linestyle='--', label='Stargate Threshold (Coherence)')
    
    plt.fill_between(time_steps, 0.85, 1.0, color='green', alpha=0.1, label='Metric Fold Zone')
    
    plt.title("The Network Auditor: Intent Coherence vs. Market Latency", fontsize=16, fontweight='bold')
    plt.xlabel("Relative Interaction Time (Sequential Pings)", fontsize=12)
    plt.ylabel("Coherence Purity Score", fontsize=12)
    plt.ylim(0.4, 1.05)
    plt.grid(True, linestyle=':', alpha=0.5)
    plt.legend(loc='lower right', framealpha=1)
    plt.tight_layout()
    plt.savefig('docs/auditor_state_sync.png')
    print("✅ Auditor State-Sync Map saved.")

    print("\n🔬 All systems coherent. All receipts generated. Ready for commit.")

if __name__ == "__main__":
    generate_lab_report()