"""
Parser for ACC driver inputs.
"""

from nordschleifen_coach.infrastructure.acc.dto.acc_driver_inputs_dto import (
    AccDriverInputsDto,
)


class DriverInputsParser:
    """
    Parses driver input data from ACC physics.
    """

    def parse(self, physics) -> AccDriverInputsDto:
        return AccDriverInputsDto(
            throttle=physics.gas,
            brake=physics.brake,
            steering=physics.steer_angle,
            clutch=physics.clutch,
            gear=physics.gear,
        )
    