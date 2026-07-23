"""
Domain model representing the dynamic behaviour of the vehicle.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class VehicleDynamics:
    """
    Represents the current dynamic state of the vehicle.
    """

    heading: float
    pitch: float
    roll: float

    velocity_x: float
    velocity_y: float
    velocity_z: float

    local_velocity_x: float
    local_velocity_y: float
    local_velocity_z: float

    g_force_x: float
    g_force_y: float
    g_force_z: float
