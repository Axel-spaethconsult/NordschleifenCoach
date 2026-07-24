"""
Maps ACC vehicle state DTOs to domain models.
"""

from nordschleifen_coach.domain.telemetry.vehicle_state import VehicleState
from nordschleifen_coach.infrastructure.acc.dto.acc_vehicle_state_dto import (
    AccVehicleStateDto,
)


class VehicleStateMapper:
    """
    Maps vehicle state DTOs to domain models.
    """

    def map(self, dto: AccVehicleStateDto) -> VehicleState:
        """
        Maps a vehicle state DTO to a domain model.
        """

        return VehicleState(
            speed=dto.speed,
            rpm=dto.rpm,
            fuel=dto.fuel,
            ignition_on=dto.ignition_on,
            engine_running=dto.engine_running,
        )