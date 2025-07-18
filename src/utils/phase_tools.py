"""
phase_tools.py

Utility functions for calculating phase alignment errors and adjustments
within IX-Secret-Fusion-Family-Recipe simulation framework.

Author: Bryce W. Design
Date: July 2025
"""

import numpy as np

def calculate_phase_alignment_error(reference_signal, test_signal):
    """
    Calculate normalized phase alignment error between two signals.

    :param reference_signal: Ideal harmonic control array.
    :param test_signal: Simulated plasma field array.
    :return: Normalized phase error value.
    """
    if len(reference_signal) != len(test_signal):
        raise ValueError("Input signals must have the same length.")

    # Calculate mean difference as simple phase error proxy
    error = np.mean(test_signal) - np.mean(reference_signal)

    return error

def apply_phase_correction(current_phase_shift, phase_error, adjustment_rate):
    """
    Adjust phase shift based on phase error and adjustment rate.

    :param current_phase_shift: Current phase shift value.
    :param phase_error: Calculated phase error.
    :param adjustment_rate: Rate at which correction is applied.
    :return: Updated phase shift.
    """
    if abs(phase_error) > 0.005:
        updated_shift = current_phase_shift - np.sign(phase_error) * adjustment_rate
    else:
        updated_shift = current_phase_shift

    return updated_shift
