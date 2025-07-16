"""
harmonic_field_model.py

Simulated harmonic field modulation algorithms inspired by Tesla 3-6-9 principles
for controlling plasma resonance and containment in the IX-Secret-Fusion-Family-Recipe.

Author: Bryce W. Design
Date: July 2025
"""

import numpy as np

class HarmonicFieldModel:
    def __init__(self, base_frequency=60.0):
        """
        Initialize harmonic field model parameters.

        :param base_frequency: Base frequency in Hz for resonance tuning.
        """
        self.base_frequency = base_frequency
        # Define 3-6-9 harmonic multipliers
        self.harmonics = [3, 6, 9]
        # Initialize storage for computed harmonic frequencies
        self.frequencies = [self.base_frequency * h for h in self.harmonics]

    def compute_resonance(self, time_array):
        """
        Compute harmonic resonance signal as the sum of sine waves at 3, 6, and 9 times the base frequency.

        :param time_array: numpy array of time points.
        :return: numpy array of resonance amplitude values.
        """
        signal = np.zeros_like(time_array)
        for freq in self.frequencies:
            signal += np.sin(2 * np.pi * freq * time_array)
        # Normalize signal
        return signal / len(self.frequencies)

    def modulate_field_strength(self, base_strength, time_array):
        """
        Modulate a base field strength with the harmonic resonance signal.

        :param base_strength: Base field strength value (float).
        :param time_array: numpy array of time points.
        :return: numpy array of modulated field strengths.
        """
        resonance = self.compute_resonance(time_array)
        return base_strength * (1 + resonance)

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    model = HarmonicFieldModel(base_frequency=60.0)
    t = np.linspace(0, 0.1, 1000)
    resonance_signal = model.compute_resonance(t)
    modulated_strength = model.modulate_field_strength(1.0, t)

    plt.plot(t, resonance_signal, label="Harmonic Resonance Signal")
    plt.plot(t, modulated_strength, label="Modulated Field Strength", linestyle="--")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.title("Tesla 3-6-9 Harmonic Field Modulation")
    plt.show()
