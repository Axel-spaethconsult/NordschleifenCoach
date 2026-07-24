"""
Application port for telemetry sources.
"""

from abc import ABC, abstractmethod

from nordschleifen_coach.domain.telemetry.telemetry_frame import (
    TelemetryFrame,
)


class TelemetrySource(ABC):
    """
    Provides telemetry frames from a telemetry backend.
    """

    @abstractmethod
    def read(self) -> TelemetryFrame | None:
        """
        Returns the latest telemetry frame.

        Returns None if no telemetry is available.
        """