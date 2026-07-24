"""
Data transfer object representing environment data read from
Assetto Corsa Competizione shared memory.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AccEnvironmentStateDto:
    """
    Raw environment values from ACC.
    """

    air_temperature: float
    track_temperature: float
    track_grip: ACC_TRACK_GRIP_STATUS
    rain_intensity: ACC_RAIN_INTENSITY
    