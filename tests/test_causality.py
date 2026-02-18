import unittest
import sys
import os

# Root anchor
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core_physics.universal_clock import UniversalClock

class TestCausality(unittest.TestCase):
    def test_standard_light_cone(self):
        """
        Verifies that an event in 'ELSEWHERE' (Space-Like separation) 
        cannot be seen by a standard observer.
        """
        clock = UniversalClock()
        
        # Event: 10 light-years away, happened 5 years ago.
        # Logic: Light needs 10 years to travel. It hasn't arrived yet.
        event = clock.check_causality(event_dist_ly=10, event_time_delta_years=5)
        
        self.assertFalse(event["visible"])
        self.assertEqual(event["status"], "ELSEWHERE")
        print(f"✅ Standard Observer Blindness Verified: {event['status']} (Lag: {event['lag_years']} yrs)")

    def test_wormhole_bypass(self):
        """
        Verifies that activating the Einstein-Rosen Bridge (Wormhole)
        allows access to 'ELSEWHERE' by reducing effective distance.
        """
        clock = UniversalClock(vacuum_index=-1) # Warp enabled
        
        # Same Event: 10 light-years away.
        # Hack: Wormhole reduces distance to ~0.
        tunnel_event = clock.activate_wormhole(target_dist_ly=10)
        
        self.assertTrue(tunnel_event["visible"])
        print(f"✅ Wormhole Bypass Verified: {tunnel_event['status']}")

if __name__ == "__main__":
    unittest.main()