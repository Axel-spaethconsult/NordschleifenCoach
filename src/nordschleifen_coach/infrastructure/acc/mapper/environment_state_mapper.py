"""
Maps ACC environment state DTOs to domain models.
"""

from nordschleifen_coach.domain.telemetry.environment_state import (
    EnvironmentState,
)
from nordschleifen_coach.infrastructure.acc.dto.acc_environment_state_dto import (
    AccEnvironmentStateDto,
)


class EnvironmentStateMapper:
    """
    Maps environment state DTOs to domain models.
    """

    def map(self, dto: AccEnvironmentStateDto) -> EnvironmentState:
        """
        Maps an environment state DTO to a domain model.
        """

        return EnvironmentState(
            air_temperature=dto.air_temperature,
            track_temperature=dto.track_temperature,
            track_grip=dto.track_grip,
            rain_intensity=dto.rain_intensity,
        )