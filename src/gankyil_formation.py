"""
gankyil_formation.py

Module implementing Gankyil formation logic for tri-spiral rotational balancing
in plasma containment and energy flow dynamics.

Author: Bryce W. Design
Date: July 2025
"""

import numpy as np

class GankyilFormation:
    def __init__(self, radius=1.0, angular_velocity=1.0):
        """
        Initialize the Gankyil formation parameters.

        :param radius: Radius of the tri-spiral arms.
        :param angular_velocity: Base angular velocity in radians per second.
        """
        self.radius = radius
        self.angular_velocity = angular_velocity
        # Three arms spaced at 120 degrees (2*pi/3 radians)
        self.phases = [0, 2 * np.pi / 3, 4 * np.pi / 3]

    def compute_positions(self, time):
        """
        Compute the (x, y) positions of the three spirals at a given time.

        :param time: Time in seconds.
        :return: List of tuples [(x1, y1), (x2, y2), (x3, y3)]
        """
        positions = []
        for phase in self.phases:
            angle = self.angular_velocity * time + phase
            x = self.radius * np.cos(angle)
            y = self.radius * np.sin(angle)
            positions.append((x, y))
        return positions

    def compute_rotational_balance(self, time):
        """
        Compute a simple scalar value representing the rotational balance
        of the tri-spiral formation at the given time.

        :param time: Time in seconds.
        :return: Rotational balance scalar (float).
        """
        positions = self.compute_positions(time)
        # For demonstration: sum of x components to indicate balance
        balance = sum(pos[0] for pos in positions)
        return balance

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    gankyil = GankyilFormation(radius=1.0, angular_velocity=2 * np.pi)
    times = np.linspace(0, 1, 500)
    balances = [gankyil.compute_rotational_balance(t) for t in times]

    plt.plot(times, balances)
    plt.title("Gankyil Formation Rotational Balance Over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Rotational Balance")
    plt.grid(True)
    plt.show()
