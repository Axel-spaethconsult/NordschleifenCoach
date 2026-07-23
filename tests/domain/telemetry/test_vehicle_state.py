"""
Tests for the VehicleState domain model.
"""

from dataclasses import FrozenInstanceError

import pytest

from nordschleifen_coach.domain.telemetry.vehicle_state import VehicleState


def test_vehicle_state_creation() -> None:
    """
    Verify that VehicleState stores all vehicle state values correctly.
    """

    state = VehicleState(
        speed=132.5,
        rpm=6150,
        fuel=42.3,
        ignition_on=True,
        engine_running=True,
    )

    assert state.speed == 132.5
    assert state.rpm == 6150
    assert state.fuel == 42.3
    assert state.ignition_on is True
    assert state.engine_running is True


def test_vehicle_state_is_immutable() -> None:
    """
    Verify that VehicleState instances are immutable.
    """

    state = VehicleState(
        speed=100.0,
        rpm=5000,
        fuel=30.0,
        ignition_on=True,
        engine_running=True,
    )

    with pytest.raises(FrozenInstanceError):
        state.speed = 150.0
