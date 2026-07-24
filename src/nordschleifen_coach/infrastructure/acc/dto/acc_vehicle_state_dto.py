"""
Data transfer object representing the vehicle state read from
Assetto Corsa Competizione shared memory.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AccVehicleStateDto:
    """
    Raw vehicle state values from ACC.
    """

    speed: float
    rpm: int
    fuel: float
    ignition_on: bool
    engine_running: bool