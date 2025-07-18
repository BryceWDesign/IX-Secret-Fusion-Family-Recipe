"""
Unit test for AdaptiveFeedbackController module in
IX-Secret-Fusion-Family-Recipe.

Author: Bryce W. Design
Date: July 2025
"""

import unittest
import numpy as np
from src.adaptive_feedback_controller import AdaptiveFeedbackController

class TestAdaptiveFeedbackController(unittest.TestCase):

    def setUp(self):
        self.controller = AdaptiveFeedbackController()

    def test_calculate_phase_error(self):
        ref_signal = np.ones(5000)
        meas_signal = np.ones(5000) * 1.05
        error = self.controller.calculate_phase_error(ref_signal, meas_signal)
        self.assertAlmostEqual(error, 0.05, places=3)

    def test_update_phase_parameters_positive_error(self):
        initial_shift = self.controller.get_current_phase_shift()
        error = 0.01  # Above default tolerance
        updated_shift = self.controller.update_phase_parameters(error)
        self.assertLess(updated_shift, initial_shift)

    def test_update_phase_parameters_below_tolerance(self):
        initial_shift = self.controller.get_current_phase_shift()
        error = 0.002  # Below default tolerance
        updated_shift = self.controller.update_phase_parameters(error)
        self.assertEqual(updated_shift, initial_shift)

if __name__ == "__main__":
    unittest.main()
