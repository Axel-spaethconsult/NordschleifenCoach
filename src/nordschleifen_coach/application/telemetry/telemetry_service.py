"""
Telemetry application service.
"""

from nordschleifen_coach.application.ports.telemetry_source import (
    TelemetrySource,
)
from nordschleifen_coach.application.telemetry.telemetry_history import (
    TelemetryHistory,
)
from nordschleifen_coach.domain.telemetry.telemetry_frame import (
    TelemetryFrame,
)


class TelemetryService:
    """
    Coordinates telemetry acquisition and history.
    """

    def __init__(
        self,
        source: TelemetrySource,
        history: TelemetryHistory,
    ):
        self._source = source
        self._history = history

    def update(self) -> TelemetryFrame | None:
        """
        Reads the latest telemetry frame and stores it.
        """

        frame = self._source.read()

        if frame is None:
            return None

        self._history.append(frame)

        return frame

    @property
    def history(self) -> TelemetryHistory:
        return self._history