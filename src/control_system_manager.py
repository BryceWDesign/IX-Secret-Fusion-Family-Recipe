"""
control_system_manager.py

Main orchestration module for IX-Secret-Fusion-Family-Recipe control system.
Integrates harmonic control engine, plasma field simulator, and feedback loop.

Author: Bryce W. Design
Date: July 2025
"""

from harmonic_control_engine import HarmonicControlEngine
from plasma_field_simulator import PlasmaFieldSimulator
import numpy as np
import matplotlib.pyplot as plt

class ControlSystemManager:
    def __init__(self):
        """
        Initialize core components.
        """
        self.harmonic_engine = HarmonicControlEngine()
        self.plasma_simulator = PlasmaFieldSimulator()

    def run_simulation_cycle(self, duration_sec=1.0, resolution=5000):
        """
        Execute a full control simulation cycle.

        :param duration_sec: Total simulation time in seconds.
        :param resolution: Number of time steps.
        :return: Tuple (time array, combined control signal, plasma field profile)
        """
        t = np.linspace(0, duration_sec, resolution)

        control_signal = self.harmonic_engine.generate_combined_field(t)
        plasma_profile = self.plasma_simulator.generate_plasma_field_profile(t)

        feedback_value = np.mean(plasma_profile) - np.mean(control_signal)
        self.harmonic_engine.update_phase_parameters(feedback_value)

        return t, control_signal, plasma_profile

    def plot_simulation_cycle(self):
        """
        Plot results from one simulation cycle.
        """
        t, control_signal, plasma_profile = self.run_simulation_cycle()

        plt.figure(figsize=(10, 6))
        plt.plot(t, control_signal, label="Harmonic Control Signal", alpha=0.8)
        plt.plot(t, plasma_profile, label="Plasma Field Profile", alpha=0.8)
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude (normalized)")
        plt.title("IX-Secret-Fusion-Family-Recipe Control System Simulation Cycle")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    manager = ControlSystemManager()
    manager.plot_simulation_cycle()
