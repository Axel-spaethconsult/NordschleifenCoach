"""
Maps ACC telemetry DTOs to domain models.
"""

from nordschleifen_coach.domain.telemetry.telemetry_frame import TelemetryFrame
from nordschleifen_coach.infrastructure.acc.dto.acc_telemetry_dto import (
    AccTelemetryDto,
)
from nordschleifen_coach.infrastructure.acc.mapper.driver_inputs_mapper import (
    DriverInputsMapper,
)
from nordschleifen_coach.infrastructure.acc.mapper.environment_state_mapper import (
    EnvironmentStateMapper,
)
from nordschleifen_coach.infrastructure.acc.mapper.session_state_mapper import (
    SessionStateMapper,
)
from nordschleifen_coach.infrastructure.acc.mapper.vehicle_dynamics_mapper import (
    VehicleDynamicsMapper,
)
from nordschleifen_coach.infrastructure.acc.mapper.vehicle_state_mapper import (
    VehicleStateMapper,
)
from nordschleifen_coach.infrastructure.acc.mapper.wheel_mapper import (
    WheelMapper,
)


class TelemetryMapper:
    """
    Maps ACC telemetry DTOs to domain telemetry frames.
    """

    def __init__(self) -> None:
        """
        Initializes all sub-mappers.
        """

        self._driver_inputs_mapper = DriverInputsMapper()
        self._vehicle_state_mapper = VehicleStateMapper()
        self._vehicle_dynamics_mapper = VehicleDynamicsMapper()
        self._wheel_mapper = WheelMapper()
        self._session_state_mapper = SessionStateMapper()
        self._environment_state_mapper = EnvironmentStateMapper()

    def map(self, dto: AccTelemetryDto) -> TelemetryFrame:
        """
        Maps an ACC telemetry DTO to a domain telemetry frame.
        """

        return TelemetryFrame(
            driver_inputs=self._driver_inputs_mapper.map(dto.driver_inputs),
            vehicle_state=self._vehicle_state_mapper.map(dto.vehicle_state),
            vehicle_dynamics=self._vehicle_dynamics_mapper.map(
                dto.vehicle_dynamics
            ),
            wheel_state=self._wheel_mapper.map(dto.wheel_state),
            session_state=self._session_state_mapper.map(dto.session_state),
            environment_state=self._environment_state_mapper.map(
                dto.environment_state
            ),
        )