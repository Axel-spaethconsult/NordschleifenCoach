"""
Data transfer object representing driver inputs read from
Assetto Corsa Competizione shared memory.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AccDriverInputsDto:
    """
    Raw driver input values from ACC.
    """

    throttle: float
    brake: float
    steering: float
    clutch: float
    gear: int