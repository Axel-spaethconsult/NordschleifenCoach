"""
Telemetry source for Assetto Corsa Competizione.
"""

from nordschleifen_coach.domain.telemetry.telemetry_frame import TelemetryFrame
from nordschleifen_coach.infrastructure.acc.mapper.telemetry_mapper import (
    TelemetryMapper,
)
from nordschleifen_coach.infrastructure.acc.parser.telemetry_parser import (
    AccTelemetryParser,
)
from nordschleifen_coach.infrastructure.acc.shared_memory.reader import (
    AccSharedMemoryReader,
)


class AccTelemetrySource:
    """
    Reads telemetry from Assetto Corsa Competizione and converts it into
    domain telemetry frames.
    """

    def __init__(self) -> None:
        self._reader = AccSharedMemoryReader()
        self._parser = AccTelemetryParser()
        self._mapper = TelemetryMapper()

    def read(self) -> TelemetryFrame:
        """
        Reads one telemetry frame.
        """

        shared_memory = self._reader.read()

        dto = self._parser.parse(shared_memory)

        return self._mapper.map(dto)