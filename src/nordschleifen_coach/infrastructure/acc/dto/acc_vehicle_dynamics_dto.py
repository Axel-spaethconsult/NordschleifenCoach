"""
Data transfer object representing vehicle dynamics read from
Assetto Corsa Competizione shared memory.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AccVehicleDynamicsDto:
    """
    Raw vehicle dynamics values from ACC.
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