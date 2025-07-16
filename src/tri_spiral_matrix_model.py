"""
tri_spiral_matrix_model.py

Simulated tri-spiral field matrix model implementing logarithmic spiral coil
geometry and harmonic field balance logic per IX-Secret-Fusion-Family-Recipe.

Author: Bryce W. Design
Date: July 2025
"""

import numpy as np
import matplotlib.pyplot as plt

class TriSpiralMatrixModel:
    def __init__(self, a=0.1, b=0.2):
        """
        Initialize spiral parameters.

        :param a: Initial radius constant for the spiral.
        :param b: Growth rate factor for the spiral.
        """
        self.a = a
        self.b = b
        self.phases = [0, 2 * np.pi / 3, 4 * np.pi / 3]  # 120-degree spacing

    def generate_spiral(self, theta_range, phase_shift):
        """
        Generate coordinates for one spiral arm.

        :param theta_range: Array of angle values.
        :param phase_shift: Phase offset in radians.
        :return: Tuple (x, y) coordinate arrays.
        """
        r = self.a * np.exp(self.b * (theta_range + phase_shift))
        x = r * np.cos(theta_range + phase_shift)
        y = r * np.sin(theta_range + phase_shift)
        return x, y

    def plot_tri_spiral(self):
        """
        Plot all three spiral arms.
        """
        theta = np.linspace(0, 4 * np.pi, 500)

        plt.figure(figsize=(6, 6))
        for phase in self.phases:
            x, y = self.generate_spiral(theta, phase)
            plt.plot(x, y, label=f"Spiral Phase {round(phase, 2)} rad")

        plt.title("Tri-Spiral Field Matrix Model")
        plt.xlabel("X Coordinate (normalized)")
        plt.ylabel("Y Coordinate (normalized)")
        plt.grid(True)
        plt.legend()
        plt.gca().set_aspect('equal', adjustable='box')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    matrix = TriSpiralMatrixModel(a=0.1, b=0.2)
    matrix.plot_tri_spiral()
