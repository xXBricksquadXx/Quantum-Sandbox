import unittest
from core_physics.universal_clock import UniversalClock

class TestChronos(unittest.TestCase):
    def test_dilation_mechanics(self):
        """Ensures Gravity slows time and Warp accelerates it."""
        well_clock = UniversalClock(observer_mass_kg=1000, vacuum_index=1)
        warp_clock = UniversalClock(observer_mass_kg=1000, vacuum_index=-1)
        
        self.assertLess(well_clock.calculate_dilation(), 1.0)
        self.assertGreater(warp_clock.calculate_dilation(), 1.0)
        print(f"✅ Dilation Logic Coherent: Well({well_clock.calculate_dilation()}) | Warp({warp_clock.calculate_dilation()})")

    def test_light_cone_enforcement(self):
        """Tests the causality boundary."""
        clock = UniversalClock()
        reachable = clock.check_causality(10, 20) # 10ly away, 20 years passed
        unreachable = clock.check_causality(50, 10) # 50ly away, 10 years passed
        
        self.assertTrue(reachable["visible"])
        self.assertFalse(unreachable["visible"])
        print("✅ Causality Gates Verified.")

if __name__ == "__main__":
    unittest.main()