"""
Data transfer object representing wheel data read from
Assetto Corsa Competizione shared memory.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AccWheelDto:
    """
    Raw wheel values from ACC.
    """

    tyre_core_temperature: float
    tyre_pressure: float
    brake_temperature: float
    brake_pressure: float
    slip_ratio: float
    slip_angle: float
    wheel_slip: float   