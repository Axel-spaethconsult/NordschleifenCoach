"""
Domain model representing the current state of the vehicle.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class VehicleState:
    """
    Represents the current operational state of the vehicle.
    """

    speed: float
    rpm: int
    fuel: float
    ignition_on: bool
    engine_running: bool
