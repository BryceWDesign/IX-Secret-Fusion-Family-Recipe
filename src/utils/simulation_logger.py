"""
simulation_logger.py

Logging utility for IX-Secret-Fusion-Family-Recipe simulation framework.
Provides consistent output formatting for monitoring harmonic and phase
alignment calculations.

Author: Bryce W. Design
Date: July 2025
"""

import logging

def setup_simulation_logger(name="IX-SFFR-Simulation"):
    """
    Set up and return a configured logger for simulation monitoring.

    :param name: Logger name identifier.
    :return: Configured logging.Logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

if __name__ == "__main__":
    logger = setup_simulation_logger()
    logger.info("IX-Secret-Fusion-Family-Recipe logger initialized.")
