"""
Parser for ACC vehicle state.
"""

from nordschleifen_coach.infrastructure.acc.dto.acc_vehicle_state_dto import (
    AccVehicleStateDto,
)


class VehicleStateParser:
    """
    Parses vehicle state data from ACC physics.
    """

    def parse(self, physics) -> AccVehicleStateDto:
        return AccVehicleStateDto(
            speed=physics.speed_kmh,
            rpm=physics.rpm,
            fuel=physics.fuel,
            ignition_on=physics.ignition_on,
            engine_running=physics.is_engine_running,
        )