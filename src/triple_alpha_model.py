"""
triple_alpha_model.py

Theoretical simulation module modeling triple-alpha fusion parameters using
Tesla 3-6-9 harmonic structuring and Gankyil phase balancing logic.

Author: Bryce W. Design
Date: July 2025
"""

import numpy as np
import matplotlib.pyplot as plt

class TripleAlphaModel:
    def __init__(self, core_density=1e20, core_temp_mk=100):
        """
        Initialize triple-alpha modeling parameters.

        :param core_density: Plasma density in particles/m³.
        :param core_temp_mk: Plasma temperature in Mega Kelvin.
        """
        self.core_density = core_density
        self.core_temp_mk = core_temp_mk
        self.gankyil_phases = [0, 120, 240]  # degrees

    def simulate_rotational_balance(self, time_array):
        """
        Simulate triple Gankyil rotational plasma balance using Tesla harmonic layering.

        :param time_array: numpy array of time points.
        :return: numpy array representing rotational balance output.
        """
        result = np.zeros_like(time_array)

        for phase_deg in self.gankyil_phases:
            phase_rad = np.deg2rad(phase_deg)
            result += np.sin(2 * np.pi * 120 * time_array + phase_rad)
            result += np.sin(2 * np.pi * 15 * time_array + phase_rad)
            result += np.sin(2 * np.pi * 0.5 * time_array + phase_rad)

        result /= (3 * 3)  # Normalize over 3 phase arms and 3 harmonics
        result *= np.exp(-time_array * (self.core_density / 1e22))

        return result

    def plot_rotational_balance(self):
        """
        Plot the simulated triple-alpha rotational balance profile.
        """
        t = np.linspace(0, 1, 5000)
        balance_profile = self.simulate_rotational_balance(t)

        plt.figure(figsize=(10, 4))
        plt.plot(t, balance_profile, label="Triple-Alpha Rotational Balance Profile")
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude (normalized)")
        plt.title("IX-Secret-Fusion-Family-Recipe Triple-Alpha Harmonic Simulation")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    model = TripleAlphaModel()
    model.plot_rotational_balance()
