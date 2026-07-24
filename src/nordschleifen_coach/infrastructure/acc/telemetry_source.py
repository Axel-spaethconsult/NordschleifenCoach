"""
ACC implementation of the telemetry source.
"""

from nordschleifen_coach.application.ports.telemetry_source import (
    TelemetrySource,
)
from nordschleifen_coach.infrastructure.acc.mapper.telemetry_mapper import (
    TelemetryMapper,
)
from nordschleifen_coach.infrastructure.acc.parser.telemetry_parser import (
    TelemetryParser,
)
from nordschleifen_coach.infrastructure.acc.shared_memory.reader import (
    AccSharedMemoryReader,
)


class AccTelemetrySource(TelemetrySource):
    """
    Reads telemetry from Assetto Corsa Competizione.
    """

    def __init__(self):
        self._reader = AccSharedMemoryReader()
        self._parser = TelemetryParser()
        self._mapper = TelemetryMapper()

    def read(self):
        raw = self._reader.read()

        if raw is None:
            return None

        dto = self._parser.parse(raw)
        return self._mapper.map(dto)

    def close(self):
        self._reader.close()