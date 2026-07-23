"""
Domain model representing the state of a single wheel.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Wheel:
    """
    Represents the telemetry of a single wheel.
    """

    tyre_core_temperature: float
    tyre_pressure: float
    brake_temperature: float
    brake_pressure: float
    slip_ratio: float
    slip_angle: float
    wheel_slip: float
