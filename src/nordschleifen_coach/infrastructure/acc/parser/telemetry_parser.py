"""
Parser orchestrating all ACC telemetry parsers.
"""

from nordschleifen_coach.infrastructure.acc.dto.acc_telemetry_dto import (
    AccTelemetryDto,
)
from nordschleifen_coach.infrastructure.acc.parser.driver_inputs_parser import (
    DriverInputsParser,
)
from nordschleifen_coach.infrastructure.acc.parser.environment_state_parser import (
    EnvironmentStateParser,
)
from nordschleifen_coach.infrastructure.acc.parser.session_state_parser import (
    SessionStateParser,
)
from nordschleifen_coach.infrastructure.acc.parser.vehicle_dynamics_parser import (
    VehicleDynamicsParser,
)
from nordschleifen_coach.infrastructure.acc.parser.vehicle_state_parser import (
    VehicleStateParser,
)
from nordschleifen_coach.infrastructure.acc.parser.wheel_parser import (
    WheelParser,
)


class TelemetryParser:
    """
    Coordinates all ACC telemetry parsers.
    """

    def __init__(self) -> None:
        self._driver_inputs_parser = DriverInputsParser()
        self._vehicle_state_parser = VehicleStateParser()
        self._vehicle_dynamics_parser = VehicleDynamicsParser()
        self._wheel_parser = WheelParser()
        self._session_state_parser = SessionStateParser()
        self._environment_state_parser = EnvironmentStateParser()

    def parse(self, shared_memory) -> AccTelemetryDto:
        physics = shared_memory.Physics
        graphics = shared_memory.Graphics
        statics = shared_memory.Static

        return AccTelemetryDto(
            driver_inputs=self._driver_inputs_parser.parse(physics),
            vehicle_state=self._vehicle_state_parser.parse(physics),
            vehicle_dynamics=self._vehicle_dynamics_parser.parse(physics),
            wheel_state=self._wheel_parser.parse(physics),
            session_state=self._session_state_parser.parse(graphics),
            environment_state=self._environment_state_parser.parse(
                physics,
                graphics,
                statics,
            ),
        )