"""
Maps ACC vehicle dynamics DTOs to domain models.
"""

from nordschleifen_coach.domain.telemetry.vehicle_dynamics import (
    VehicleDynamics,
)
from nordschleifen_coach.infrastructure.acc.dto.acc_vehicle_dynamics_dto import (
    AccVehicleDynamicsDto,
)


class VehicleDynamicsMapper:
    """
    Maps vehicle dynamics DTOs to domain models.
    """

    def map(self, dto: AccVehicleDynamicsDto) -> VehicleDynamics:
        """
        Maps a vehicle dynamics DTO to a domain model.
        """

        return VehicleDynamics(
            heading=dto.heading,
            pitch=dto.pitch,
            roll=dto.roll,

            velocity_x=dto.velocity_x,
            velocity_y=dto.velocity_y,
            velocity_z=dto.velocity_z,

            local_velocity_x=dto.local_velocity_x,
            local_velocity_y=dto.local_velocity_y,
            local_velocity_z=dto.local_velocity_z,

            g_force_x=dto.g_force_x,
            g_force_y=dto.g_force_y,
            g_force_z=dto.g_force_z,
        )