import numpy as np
from core_physics.universal_clock import UniversalClock
from core_physics.neuro_state import NeuroSubsystem

class AuditorLogic:
    def __init__(self, observer_mass=70, vacuum_index=-1):
        self.clock = UniversalClock(observer_mass_kg=observer_mass, vacuum_index=vacuum_index)
        self.ideal_intent = np.array([1, 0])
        self.reference_rho = np.outer(self.ideal_intent, np.conj(self.ideal_intent))
        self.observer = NeuroSubsystem(self.ideal_intent)
        self.topological_braid = []

    def audit_environment(self):
        system_report = self.clock.tick()
        dilation = system_report["Dilation_Factor"]
        # Shielding factor: reduces solar flare impact on the Auditor
        interference_penalty = len(system_report["Interrupts"]) * 0.02 
        return dilation, interference_penalty

    def process_intent_state(self, raw_input_string):
        """
        State-Sync Discriminator: Converts strings to non-linear state pulses.
        """
        unique_chars = len(set(raw_input_string))
        total_chars = len(raw_input_string)
        char_variance = unique_chars / total_chars if total_chars > 0 else 0
        
        # GOLDILOCKS GATE: Slop filtering based on complexity
        if char_variance < 0.35 or char_variance > 0.85:
            spirit_penalty = 0.5 # Immediate decoherence for slop
        else:
            spirit_penalty = 0.02
            
        entropy_tilt = (sum(ord(c) for c in raw_input_string) % 50 / 100.0) + spirit_penalty
        dilation, penalty = self.audit_environment()
        
        # Noise floor tuned for 'Elsewhere' operation
        noise_level = 0.05 + penalty + entropy_tilt
        
        # Interaction with the field
        self.observer.rho = (1 - noise_level) * self.observer.rho + \
                            (noise_level) * np.eye(2) * 0.5
        
        # TESLA BYPASS: Instant correction pulse
        if noise_level > 0.10:
            self.observer.apply_error_correction(self.reference_rho)
        
        purity = self.observer.get_purity()
        
        self.topological_braid.append({
            "purity": purity,
            "dilation": dilation,
            "locked": purity > 0.88 
        })

        return {
            "purity_score": purity,
            "causal_status": "SYNCHRONIZED" if purity > 0.88 else "DECOHERED"
        }

    def generate_stargate_receipt(self):
        if not self.topological_braid: return "NO_DATA"
        
        # EVALUATION: Look at the peak stability of the braid
        # If the observer achieves a lock at any point in the recent pulses, 
        # the metric fold is validated.
        recent_purity = [b["purity"] for b in self.topological_braid[-5:]]
        max_stability = max(recent_purity)
        
        if max_stability > 0.90: 
            return "RECEIPT: Metric Fold Successful. Information Tunnel Open."
        else:
            return "RECEIPT: Insufficient Coherence. Signal limited to Light Cone."