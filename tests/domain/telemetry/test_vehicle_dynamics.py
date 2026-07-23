"""
Tests for the VehicleDynamics domain model.
"""

from dataclasses import FrozenInstanceError

import pytest

from nordschleifen_coach.domain.telemetry.vehicle_dynamics import (
    VehicleDynamics,
)


def test_vehicle_dynamics_creation() -> None:
    """
    Verify that VehicleDynamics stores all dynamic values correctly.
    """

    dynamics = VehicleDynamics(
        heading=180.0,
        pitch=1.5,
        roll=-0.3,
        velocity_x=10.0,
        velocity_y=2.5,
        velocity_z=0.0,
        local_velocity_x=9.8,
        local_velocity_y=0.2,
        local_velocity_z=0.0,
        g_force_x=0.8,
        g_force_y=1.2,
        g_force_z=0.0,
    )

    assert dynamics.heading == 180.0
    assert dynamics.pitch == 1.5
    assert dynamics.roll == -0.3

    assert dynamics.velocity_x == 10.0
    assert dynamics.velocity_y == 2.5
    assert dynamics.velocity_z == 0.0

    assert dynamics.local_velocity_x == 9.8
    assert dynamics.local_velocity_y == 0.2
    assert dynamics.local_velocity_z == 0.0

    assert dynamics.g_force_x == 0.8
    assert dynamics.g_force_y == 1.2
    assert dynamics.g_force_z == 0.0


def test_vehicle_dynamics_is_immutable() -> None:
    """
    Verify that VehicleDynamics instances are immutable.
    """

    dynamics = VehicleDynamics(
        heading=0.0,
        pitch=0.0,
        roll=0.0,
        velocity_x=0.0,
        velocity_y=0.0,
        velocity_z=0.0,
        local_velocity_x=0.0,
        local_velocity_y=0.0,
        local_velocity_z=0.0,
        g_force_x=0.0,
        g_force_y=0.0,
        g_force_z=0.0,
    )

    with pytest.raises(FrozenInstanceError):
        dynamics.heading = 90.0
