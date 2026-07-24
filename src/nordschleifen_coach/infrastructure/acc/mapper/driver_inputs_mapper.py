"""
Maps ACC driver input DTOs to domain models.
"""

from nordschleifen_coach.domain.telemetry.driver_inputs import DriverInputs
from nordschleifen_coach.infrastructure.acc.dto.acc_driver_inputs_dto import (
    AccDriverInputsDto,
)


class DriverInputsMapper:
    """
    Maps driver input DTOs to domain models.
    """

    def map(self, dto: AccDriverInputsDto) -> DriverInputs:
        """
        Maps a driver input DTO to a domain model.
        """

        return DriverInputs(
            steering=dto.steering,
            throttle=dto.throttle,
            brake=dto.brake,
            clutch=dto.clutch,
            gear=dto.gear,
        )