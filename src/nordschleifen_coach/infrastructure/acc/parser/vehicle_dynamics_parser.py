"""
Parser for ACC vehicle dynamics.
"""

from nordschleifen_coach.infrastructure.acc.dto.acc_vehicle_dynamics_dto import (
    AccVehicleDynamicsDto,
)


class VehicleDynamicsParser:
    """
    Parses vehicle dynamics data from ACC physics.
    """

    def parse(self, physics) -> AccVehicleDynamicsDto:
        return AccVehicleDynamicsDto(
            heading=physics.heading,
            pitch=physics.pitch,
            roll=physics.roll,
            velocity_x=physics.velocity.x,
            velocity_y=physics.velocity.y,
            velocity_z=physics.velocity.z,
            local_velocity_x=physics.local_velocity.x,
            local_velocity_y=physics.local_velocity.y,
            local_velocity_z=physics.local_velocity.z,
            g_force_x=physics.g_force.x,
            g_force_y=physics.g_force.y,
            g_force_z=physics.g_force.z,
        )