"""
Domain model representing the current session state.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SessionState:
    """
    Represents the current state of the driving session.
    """

    lap_number: int
    lap_time: float
    best_lap_time: float
    is_valid_lap: bool
    normalized_position: float
    distance_travelled: float
