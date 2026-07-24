"""
Evaluates driving events and produces coaching feedback.
"""

from nordschleifen_coach.application.coaching.driving_event import (
    DrivingEvent,
)
from nordschleifen_coach.application.coaching.driving_state import (
    DrivingState,
)
from nordschleifen_coach.application.telemetry.telemetry_history import (
    TelemetryHistory,
)


class CoachEngine:
    """
    Evaluates the current driving situation.
    """

    def evaluate(
        self,
        state: DrivingState,
        event: DrivingEvent,
        history: TelemetryHistory,
    ) -> str | None:

        if event == DrivingEvent.BRAKE_STARTED:
            return "Brake started."

        if event == DrivingEvent.BRAKE_RELEASED:
            return "Brake released."

        if event == DrivingEvent.ACCELERATION_STARTED:
            return "Acceleration started."

        if event == DrivingEvent.ACCELERATION_ENDED:
            return "Acceleration ended."

        return None