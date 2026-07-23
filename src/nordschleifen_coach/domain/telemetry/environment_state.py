"""
Domain model representing the current environmental conditions.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EnvironmentState:
    """
    Represents the environmental conditions affecting the vehicle.
    """

    air_temperature: float
    track_temperature: float
    track_grip: float
    rain_intensity: float
