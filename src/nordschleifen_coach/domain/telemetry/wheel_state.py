"""
Domain model representing the state of all four wheels.
"""

from dataclasses import dataclass

from nordschleifen_coach.domain.telemetry.wheel import Wheel


@dataclass(frozen=True, slots=True)
class WheelState:
    """
    Represents the telemetry of all four wheels.
    """

    front_left: Wheel
    front_right: Wheel
    rear_left: Wheel
    rear_right: Wheel
