"""
Represents driving events derived from state changes.
"""

from enum import Enum


class DrivingEvent(Enum):
    """
    High-level driving events.
    """

    NONE = "none"

    BRAKE_STARTED = "brake_started"
    BRAKE_RELEASED = "brake_released"

    ACCELERATION_STARTED = "acceleration_started"
    ACCELERATION_ENDED = "acceleration_ended"