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
    
    # Note: Qiskit handles internal labeling for histograms, but we save it cleanly.
    plot_histogram(counts, title="Manifestation Probability (State Collapse)").savefig('docs/manifestation_probabilities.png')
    print("✅ Manifestation Histogram saved.")

    # 3. Energy Index Chart
    # ---------------------------------------------------------
    levels = np.array([-1, 0, 1, 2])
    labels = ['Dirac Sea (-1)', 'Ground (0)', 'L=1 (Hydrogen)', 'L=2 (Hydrogen)']
    
    plt.figure(figsize=(10, 6)) # Wider for readability
    plt.hlines(levels, 0, 1, colors=['red', 'black', 'blue', 'green'], linewidth=2)
    
    for i, txt in enumerate(labels): 
        plt.annotate(txt, (1.02, levels[i]), fontsize=12, verticalalignment='center')
    
    plt.title("Quantum State Array: Global Energy Indices", fontsize=14, fontweight='bold')
    plt.ylabel("Energy Eigenvalues (n)", fontsize=12)
    plt.xlabel("System Breadth (Arbitrary Units)", fontsize=12)
    plt.xticks([]) # X-axis is purely demonstrative here
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
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.savefig('docs/vibration_mass_slope.png')
    print("✅ Vibration-Mass Slope saved.")

    # 5. Neuro-Purity Recovery
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
    # Origin 'lower' puts (0,0) at bottom-left
    plt.imshow(p_map, extent=[0, 1, 0, 1], origin='lower', cmap='plasma', aspect='auto')
    
    cbar = plt.colorbar()
    cbar.set_label(r'Purity Score [$Tr(\rho^2)$]', fontsize=12)
    
    plt.title("Neuro-Quantum Recovery: Phased Array Efficiency", fontsize=14, fontweight='bold')
    plt.xlabel("Correction Strength (Phased Array Intensity)", fontsize=12)
    plt.ylabel("Noise Level (Environmental Decoherence)", fontsize=12)
    plt.tight_layout()
    plt.savefig('docs/neuro_purity_recovery.png')
    print("✅ Neuro-Purity Heatmap saved.")

    # 6. Chronos Dilation Map
    # ---------------------------------------------------------
    print("⏳ Generating Relativistic Dilation Map...")
    mass_range = np.linspace(1, 100000, 20)
    v_indices = np.linspace(-1, 1, 20)
    d_map = np.zeros((20, 20))
    
    for i, m in enumerate(mass_range):
        for j, v in enumerate(v_indices):
            clock = UniversalClock(observer_mass_kg=m, vacuum_index=v)
            d_map[i, j] = clock.calculate_dilation()
            
    plt.figure(figsize=(10, 8))
    plt.imshow(d_map, extent=[-1, 1, 1, 100000], aspect='auto', origin='lower', cmap='viridis')
    
    cbar = plt.colorbar()
    cbar.set_label(r'Dilation Factor ($t_{obs} / t_{univ}$)', fontsize=12)
    
    plt.title("Project Chronos: Relativistic Time Dilation", fontsize=14, fontweight='bold')
    plt.xlabel("Vacuum Index (Negative = Warp | Positive = Gravity)", fontsize=12)
    plt.ylabel("Observer Mass (kg)", fontsize=12)
    plt.tight_layout()
    plt.savefig('docs/chronos_dilation_map.png')
    print("✅ Chronos Dilation Map saved.")

    # 7. Causality & Wormhole Visualization
    # ---------------------------------------------------------
    print("⏳ Generating Light Cone & Wormhole Topology...")
    
    x = np.linspace(-15, 15, 100) # Space
    
    plt.figure(figsize=(10, 10))
    
    # Plot the Light Cone (The "Box")
    plt.fill_between(x, np.abs(x), 15, color='#d3d3d3', alpha=0.4, label='Causal Future (The Cone)')
    
    # Plot the "ELSEWHERE" Event
    event_x = 10
    event_t = 5
    plt.plot(event_x, event_t, 'ro', markersize=12, markeredgecolor='black', label='Event in ELSEWHERE')
    
    # Plot the Observer
    plt.plot(0, 0, 'bo', markersize=12, markeredgecolor='black', label='Observer (Now)')
    
    # Plot the Wormhole Tunnel
    plt.annotate('', xy=(event_x, event_t), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='<->', color='#32CD32', lw=3, linestyle='--')) # Lime Green
    plt.text(5, 1.5, r'Wormhole Tunnel ($ds^2 \approx 0$)', color='green', fontsize=12, rotation=25, fontweight='bold')

    # IBM Style Formatting
    plt.axhline(0, color='black', linewidth=1.5)
    plt.axvline(0, color='black', linewidth=1.5)
    plt.grid(True, linestyle=':', alpha=0.6)
    
    plt.title("Relativistic Causality: The Wormhole Bypass", fontsize=16, fontweight='bold')
    plt.xlabel("Space (Light Years)", fontsize=14)
    plt.ylabel("Time (Years)", fontsize=14)
    plt.legend(loc='upper left', fontsize=12, frameon=True, facecolor='white', framealpha=1)
    plt.xlim(-12, 12)
    plt.ylim(0, 12)
    plt.tight_layout()
    
    plt.savefig('docs/light_cone_bypass.png')
    print("✅ Light Cone Bypass Graph saved.")
    
    print("\n🔬 All systems coherent. Ready for commit.")

if __name__ == "__main__":
    generate_lab_report()