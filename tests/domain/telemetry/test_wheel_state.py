"""
Tests for the WheelState domain model.
"""

from dataclasses import FrozenInstanceError

import pytest

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


def test_wheel_state_creation() -> None:
    """
    Verify that WheelState stores all four wheels correctly.
    """

    wheels = WheelState(
        front_left=create_wheel(),
        front_right=create_wheel(),
        rear_left=create_wheel(),
        rear_right=create_wheel(),
    )

    assert wheels.front_left.tyre_pressure == 27.0
    assert wheels.front_right.tyre_pressure == 27.0
    assert wheels.rear_left.tyre_pressure == 27.0
    assert wheels.rear_right.tyre_pressure == 27.0


def test_wheel_state_is_immutable() -> None:
    """
    Verify that WheelState instances are immutable.
    """

    wheels = WheelState(
        front_left=create_wheel(),
        front_right=create_wheel(),
        rear_left=create_wheel(),
        rear_right=create_wheel(),
    )

    with pytest.raises(FrozenInstanceError):
        wheels.front_left = create_wheel()
