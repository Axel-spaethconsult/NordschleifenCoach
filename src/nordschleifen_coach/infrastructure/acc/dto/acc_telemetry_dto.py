"""
Aggregate data transfer object representing a complete telemetry
snapshot read from Assetto Corsa Competizione shared memory.
"""

from dataclasses import dataclass

from nordschleifen_coach.infrastructure.acc.dto.acc_driver_inputs_dto import (
    AccDriverInputsDto,
)
from nordschleifen_coach.infrastructure.acc.dto.acc_environment_state_dto import (
    AccEnvironmentStateDto,
)
from nordschleifen_coach.infrastructure.acc.dto.acc_session_state_dto import (
    AccSessionStateDto,
)
from nordschleifen_coach.infrastructure.acc.dto.acc_vehicle_dynamics_dto import (
    AccVehicleDynamicsDto,
)
from nordschleifen_coach.infrastructure.acc.dto.acc_vehicle_state_dto import (
    AccVehicleStateDto,
)
from nordschleifen_coach.infrastructure.acc.dto.acc_wheel_state_dto import (
    AccWheelStateDto,
)


@dataclass(frozen=True, slots=True)
class AccTelemetryDto:
    """
    Complete raw telemetry snapshot from ACC.
    """

    driver_inputs: AccDriverInputsDto
    vehicle_state: AccVehicleStateDto
    vehicle_dynamics: AccVehicleDynamicsDto
    wheel_state: AccWheelStateDto
    session_state: AccSessionStateDto
    environment_state: AccEnvironmentStateDto