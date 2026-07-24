"""
Parser for ACC environment state.
"""

from nordschleifen_coach.infrastructure.acc.dto.acc_environment_state_dto import (
    AccEnvironmentStateDto,
)


class EnvironmentStateParser:

    def parse(
        self,
        physics,
        graphics,
        statics,  # derzeit ungenutzt
    ) -> AccEnvironmentStateDto:
        return AccEnvironmentStateDto(
            air_temperature=physics.air_temp,
            track_temperature=physics.road_temp,
            track_grip=graphics.track_grip_status,
            rain_intensity=graphics.rain_intensity,
        )    