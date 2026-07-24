"""
Detects the current driving state from telemetry.
"""

from nordschleifen_coach.application.telemetry.telemetry_history import (
    TelemetryHistory,
)

from .driving_state import DrivingState


class DrivingStateDetector:
    """
    Detects the current high-level driving state.
    """

    BRAKE_THRESHOLD = 0.05
    THROTTLE_THRESHOLD = 0.05
    IDLE_SPEED_THRESHOLD = 1.0

    def detect(self, history: TelemetryHistory) -> DrivingState:
        frame = history.latest()

        if frame is None:
            return DrivingState.UNKNOWN

        # Driver inputs have priority
        if frame.driver_inputs.brake > self.BRAKE_THRESHOLD:
            return DrivingState.BRAKING

        if frame.driver_inputs.throttle > self.THROTTLE_THRESHOLD:
            return DrivingState.ACCELERATING

        # Vehicle state
        if frame.vehicle_state.speed <= self.IDLE_SPEED_THRESHOLD:
            return DrivingState.IDLE

        return DrivingState.COASTING