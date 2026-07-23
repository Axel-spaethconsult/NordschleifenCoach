"""
Domain model representing driver control inputs.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DriverInputs:
    """
    Represents the driver's control inputs at a single point in time.
    """

    throttle: float
    brake: float
    steering: float
    clutch: float
    gear: int
