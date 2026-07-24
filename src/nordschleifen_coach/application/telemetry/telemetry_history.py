"""
Stores a rolling history of telemetry frames.
"""

from collections import deque

from nordschleifen_coach.domain.telemetry.telemetry_frame import (
    TelemetryFrame,
)


class TelemetryHistory:
    """
    Stores the most recent telemetry frames.
    """

    def __init__(self, max_frames: int = 200):
        self._frames = deque(maxlen=max_frames)

    def append(self, frame: TelemetryFrame) -> None:
        """
        Appends a telemetry frame.
        """
        self._frames.append(frame)

    def latest(self) -> TelemetryFrame | None:
        """
        Returns the most recent frame.
        """
        if not self._frames:
            return None

        return self._frames[-1]

    def last(self, count: int) -> list[TelemetryFrame]:
        """
        Returns the newest 'count' frames.
        """
        return list(self._frames)[-count:]

    def clear(self) -> None:
        """
        Clears the history.
        """
        self._frames.clear()

    def __len__(self) -> int:
        return len(self._frames)