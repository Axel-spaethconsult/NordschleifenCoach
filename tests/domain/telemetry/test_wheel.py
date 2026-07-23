"""
Tests for the Wheel domain model.
"""

from dataclasses import FrozenInstanceError

import pytest

from nordschleifen_coach.domain.telemetry.wheel import Wheel


def test_wheel_creation() -> None:
    """
    Verify that Wheel stores all telemetry values correctly.
    """

    wheel = Wheel(
        tyre_core_temperature=82.5,
        tyre_pressure=27.4,
        brake_temperature=515.0,
        brake_pressure=0.85,
        slip_ratio=0.03,
        slip_angle=1.8,
        wheel_slip=0.02,
    )

    assert wheel.tyre_core_temperature == 82.5
    assert wheel.tyre_pressure == 27.4
    assert wheel.brake_temperature == 515.0
    assert wheel.brake_pressure == 0.85
    assert wheel.slip_ratio == 0.03
    assert wheel.slip_angle == 1.8
    assert wheel.wheel_slip == 0.02


def test_wheel_is_immutable() -> None:
    """
    Verify that Wheel instances are immutable.
    """

    wheel = Wheel(
        tyre_core_temperature=80.0,
        tyre_pressure=27.0,
        brake_temperature=500.0,
        brake_pressure=0.5,
        slip_ratio=0.0,
        slip_angle=0.0,
        wheel_slip=0.0,
    )

    with pytest.raises(FrozenInstanceError):
        wheel.tyre_pressure = 28.0
