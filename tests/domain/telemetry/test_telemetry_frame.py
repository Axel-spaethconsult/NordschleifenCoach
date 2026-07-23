"""
Tests for the TelemetryFrame domain model.
"""

from dataclasses import FrozenInstanceError

import pytest

from nordschleifen_coach.domain.telemetry.driver_inputs import DriverInputs
from nordschleifen_coach.domain.telemetry.environment_state import (
    EnvironmentState,
)
from nordschleifen_coach.domain.telemetry.session_state import SessionState
from nordschleifen_coach.domain.telemetry.telemetry_frame import (
    TelemetryFrame,
)
from nordschleifen_coach.domain.telemetry.vehicle_dynamics import (
    VehicleDynamics,
)
from nordschleifen_coach.domain.telemetry.vehicle_state import VehicleState
from nordschleifen_coach.domain.telemetry.wheel import Wheel
from nordschleifen_coach.domain.telemetry.wheel_state import WheelState


def create_wheel() -> Wheel:
    """
    Create a wheel instance for testing.
    """

    return Wheel(
        tyre_core_temperature=80.0,
        tyre_pressure=27.0,
        brake_temperature=500.0,
        brake_pressure=0.5,
        slip_ratio=0.0,
        slip_angle=0.0,
        wheel_slip=0.0,
    )


def create_wheel_state() -> WheelState:
    """
    Create a wheel state instance for testing.
    """

    wheel = create_wheel()

    return WheelState(
        front_left=wheel,
        front_right=wheel,
        rear_left=wheel,
        rear_right=wheel,
    )


def test_telemetry_frame_creation() -> None:
    """
    Verify that TelemetryFrame stores all telemetry components correctly.
    """

    frame = TelemetryFrame(
        driver_inputs=DriverInputs(
            throttle=0.8,
            brake=0.0,
            steering=0.1,
            clutch=0.0,
            gear=4,
        ),
        vehicle_state=VehicleState(
            speed=145.2,
            rpm=6200,
            fuel=42.5,
            ignition_on=True,
            engine_running=True,
        ),
        vehicle_dynamics=VehicleDynamics(
            heading=180.0,
            pitch=0.2,
            roll=-0.1,
            velocity_x=10.0,
            velocity_y=0.5,
            velocity_z=0.0,
            local_velocity_x=9.8,
            local_velocity_y=0.2,
            local_velocity_z=0.0,
            g_force_x=0.1,
            g_force_y=1.2,
            g_force_z=0.0,
        ),
        wheel_state=create_wheel_state(),
        session_state=SessionState(
            lap_number=3,
            lap_time=91.2,
            best_lap_time=90.8,
            is_valid_lap=True,
            normalized_position=0.42,
            distance_travelled=12500.0,
        ),
        environment_state=EnvironmentState(
            air_temperature=22.0,
            track_temperature=31.5,
            track_grip=1.0,
            rain_intensity=0.0,
        ),
    )

    assert frame.driver_inputs.gear == 4
    assert frame.vehicle_state.speed == 145.2
    assert frame.vehicle_dynamics.heading == 180.0
    assert frame.wheel_state.front_left.tyre_pressure == 27.0
    assert frame.session_state.lap_number == 3
    assert frame.environment_state.track_temperature == 31.5


def test_telemetry_frame_is_immutable() -> None:
    """
    Verify that TelemetryFrame instances are immutable.
    """

    frame = TelemetryFrame(
        driver_inputs=DriverInputs(0.0, 0.0, 0.0, 0.0, 1),
        vehicle_state=VehicleState(0.0, 0, 0.0, False, False),
        vehicle_dynamics=VehicleDynamics(
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ),
        wheel_state=create_wheel_state(),
        session_state=SessionState(1, 0.0, 0.0, True, 0.0, 0.0),
        environment_state=EnvironmentState(0.0, 0.0, 1.0, 0.0),
    )

    with pytest.raises(FrozenInstanceError):
        frame.driver_inputs = DriverInputs(1.0, 0.0, 0.0, 0.0, 2)
