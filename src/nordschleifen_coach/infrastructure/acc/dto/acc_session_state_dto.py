"""
Data transfer object representing session state read from
Assetto Corsa Competizione shared memory.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AccSessionStateDto:
    """
    Raw session state values from ACC.
    """

    lap_number: int
    lap_time: float
    best_lap_time: float
    is_valid_lap: bool
    normalized_position: float
    distance_travelled: float