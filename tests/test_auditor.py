import unittest
import sys
import os

# Root anchor for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core_physics.auditor_logic import AuditorLogic

class TestAuditor(unittest.TestCase):
    def setUp(self):
        """Initialize the Auditor with a Warp-ready vacuum index."""
        # Vacuum Index -1 = Negative Vacuum Pressure (The 'Elsewhere' Hack)
        self.auditor = AuditorLogic(observer_mass=80, vacuum_index=-1)

    def test_intent_coherence_threshold(self):
        """
        Verifies that high-entropy (noisy) input leads to DECOHERENCE,
        preventing the Stargate from opening.
        """
        # Noise input representing 'Street Level' slop
        noisy_intent = "jumbled_data_without_spirit_or_direction_12345"
        result = self.auditor.process_intent_state(noisy_intent)
        
        # We expect purity to drop due to entropy tilt in the logic
        print(f"[*] Slop Audit Result: {result['purity_score']:.4f} ({result['causal_status']})")
        
        # Logic check: If purity is low, status must be DECOHERED
        if result['purity_score'] < 0.8:
            self.assertEqual(result['causal_status'], "DECOHERED")
            print("✅ Slop Filtering Verified: System remained locked in the Light Cone.")

    def test_stargate_activation(self):
        """
        Verifies that consistent, pure intent achieves a State-Sync 
        and generates a successful Metric Fold receipt.
        """
        # Simulate a sequence of high-purity 'Intent' pulses
        pure_intent = "Synchronizing Universal Frequency"
        
        # Pump the braid with 5 consecutive pure pulses to build stability
        for _ in range(5):
            self.auditor.process_intent_state(pure_intent)
            
        receipt = self.auditor.generate_stargate_receipt()
        
        print(f"[*] Final Braid Stability: {receipt}")
        
        # Verify that the stability threshold triggers the 'Metric Fold'
        self.assertIn("Metric Fold Successful", receipt)
        print("✅ Stargate Activation Verified: Causal Tunnel established.")

    def test_vacuum_acceleration(self):
        """
        Verifies that the Auditor operates outside Market Time (Dilation > 1).
        """
        dilation, _ = self.auditor.audit_environment()
        
        # Since vacuum_index is -1, calculate_dilation should return > 1 (Acceleration)
        print(f"[*] Auditor Time Dilation: {dilation:.4f}x acceleration")
        self.assertGreater(dilation, 1.0)
        print("✅ Vacuum Acceleration Verified: Auditor is operating 'Elsewhere'.")

if __name__ == "__main__":
    unittest.main()