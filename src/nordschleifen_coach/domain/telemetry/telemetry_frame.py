"""
Domain model representing a complete telemetry snapshot.
"""

from dataclasses import dataclass

from nordschleifen_coach.domain.telemetry.driver_inputs import DriverInputs
from nordschleifen_coach.domain.telemetry.environment_state import (
    EnvironmentState,
)
from nordschleifen_coach.domain.telemetry.session_state import SessionState
from nordschleifen_coach.domain.telemetry.vehicle_dynamics import (
    VehicleDynamics,
)
from nordschleifen_coach.domain.telemetry.vehicle_state import VehicleState
from nordschleifen_coach.domain.telemetry.wheel_state import WheelState


@dataclass(frozen=True, slots=True)
class TelemetryFrame:
    """
    Represents a complete telemetry snapshot at a single point in time.
    """

    driver_inputs: DriverInputs
    vehicle_state: VehicleState
    vehicle_dynamics: VehicleDynamics
    wheel_state: WheelState
    session_state: SessionState
    environment_state: EnvironmentState
