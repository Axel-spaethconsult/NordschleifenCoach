"""
Maps ACC wheel DTOs to domain models.
"""

from nordschleifen_coach.domain.telemetry.wheel import Wheel
from nordschleifen_coach.domain.telemetry.wheel_state import WheelState
from nordschleifen_coach.infrastructure.acc.dto.acc_wheel_dto import (
    AccWheelDto,
)
from nordschleifen_coach.infrastructure.acc.dto.acc_wheel_state_dto import (
    AccWheelStateDto,
)


class WheelMapper:
    """
    Maps wheel DTOs to domain models.
    """

    def _map_wheel(self, dto: AccWheelDto) -> Wheel:
        """
        Maps a single wheel DTO to a domain wheel model.
        """

        return Wheel(
            tyre_core_temperature=dto.tyre_core_temperature,
            tyre_pressure=dto.tyre_pressure,
            brake_temperature=dto.brake_temperature,
            brake_pressure=dto.brake_pressure,
            slip_ratio=dto.slip_ratio,
            slip_angle=dto.slip_angle,
            wheel_slip=dto.wheel_slip,
        )

    def map(self, dto: AccWheelStateDto) -> WheelState:
        """
        Maps a wheel state DTO to a domain model.
        """

        return WheelState(
            front_left=self._map_wheel(dto.front_left),
            front_right=self._map_wheel(dto.front_right),
            rear_left=self._map_wheel(dto.rear_left),
            rear_right=self._map_wheel(dto.rear_right),
        )