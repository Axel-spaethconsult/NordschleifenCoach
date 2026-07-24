"""
Detects driving events from driving state changes.
"""

from .driving_event import DrivingEvent
from .driving_state import DrivingState


class DrivingEventDetector:
    """
    Detects high-level driving events.
    """

    def __init__(self) -> None:
        self._previous_state = DrivingState.UNKNOWN

    def detect(self, current_state: DrivingState) -> DrivingEvent:
        previous = self._previous_state
        self._previous_state = current_state

        if (
            previous != DrivingState.BRAKING
            and current_state == DrivingState.BRAKING
        ):
            return DrivingEvent.BRAKE_STARTED

        if (
            previous == DrivingState.BRAKING
            and current_state != DrivingState.BRAKING
        ):
            return DrivingEvent.BRAKE_RELEASED

        if (
            previous != DrivingState.ACCELERATING
            and current_state == DrivingState.ACCELERATING
        ):
            return DrivingEvent.ACCELERATION_STARTED

        if (
            previous == DrivingState.ACCELERATING
            and current_state != DrivingState.ACCELERATING
        ):
            return DrivingEvent.ACCELERATION_ENDED

        return DrivingEvent.NONE