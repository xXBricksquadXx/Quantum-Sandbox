import random
import math

class UniversalClock:
    def __init__(self, observer_mass_kg=70, vacuum_index=0):
        """
        Initializes the Universal Clock.
        :param observer_mass_kg: The 'Presence' (Mass/Energy) of the observer.
        :param vacuum_index: 0 = Earth Standard. Negative = Anti-Gravity (Dirac Sea).
        """
        # Physics Constants
        self.PLANCK_TIME = 5.39e-44 
        self.SPEED_OF_LIGHT = 299792458 # m/s
        self.GRAVITATIONAL_CONSTANT = 6.674e-11 
        
        # State
        self.observer_mass = observer_mass_kg
        self.vacuum_index = vacuum_index
        self.entropy_state = 0.0
        self.total_planck_ticks = 0
        
        # Cosmic State (Simulated)
        self.solar_flare_active = False
        self.nearby_supernova_dist = 640 # light years (Betelgeuse)

    def calculate_dilation(self):
        """Calculates Time Dilation based on Gravity/Vacuum Pressure."""
        # Simplified Schwarzschild metric logic
        gravity_load = self.observer_mass * (1 + abs(self.vacuum_index))
        
        if self.vacuum_index < 0:
            # Negative Energy (Warp Bubble) -> Time Acceleration
            return 1 + (gravity_load / 1000)
        else:
            # Positive Mass (Gravity Well) -> Time Dilation (Slowing)
            return 1 - (gravity_load / 100000)

    def check_causality(self, event_dist_ly, event_time_delta_years):
        """Enforces the Light Cone (The Box)."""
        if event_dist_ly > event_time_delta_years:
            latency = event_dist_ly - event_time_delta_years
            return {"status": "ELSEWHERE", "visible": False, "lag_years": latency}
        else:
            return {"status": "CAUSAL_LINK", "visible": True, "lag_years": 0}

    def check_cosmic_interrupts(self):
        """Checks for external variables (The Sun, Supernovas)."""
        interrupts = []
        
        if random.random() < 0.05: # 5% chance of flare
            self.solar_flare_active = True
            interrupts.append("SOLAR_CME_DETECTED: Resonance Shift +3.5Hz")
            
        causality = self.check_causality(self.nearby_supernova_dist, 640)
        
        if causality["visible"]:
             interrupts.append("SUPERNOVA_PACKET_RECEIVED: Gravity Wave Detected")
        else:
             interrupts.append(f"SUPERNOVA_PENDING: Packet Lag {causality['lag_years']} years")
             
        return interrupts

    def activate_wormhole(self, target_dist_ly):
        """Bypasses the Light Cone using an Einstein-Rosen Bridge."""
        print(f"[*] ACTIVATING BRIDGE. Target: {target_dist_ly} ly")
        print(f"[*] TUNNELING through Hypersurface...")
        return self.check_causality(0.0000001, 1)

    def tick(self, duration_sec=1):
        dilation = self.calculate_dilation()
        experienced_time = duration_sec * dilation
        
        self.entropy_state += (random.uniform(0.001, 0.005) * self.observer_mass)
        self.total_planck_ticks += (experienced_time / self.PLANCK_TIME)
        
        return {
            "Market_Time": duration_sec,
            "Universal_Time": experienced_time,
            "Dilation_Factor": dilation,
            "Interrupts": self.check_cosmic_interrupts()
        }

if __name__ == "__main__":
    clock = UniversalClock(observer_mass_kg=80, vacuum_index=0)
    print("--- SYSTEM START ---")
    print(clock.tick(1))
    print("\n--- ATTEMPTING BRIDGE ---")
    print(clock.activate_wormhole(1000))