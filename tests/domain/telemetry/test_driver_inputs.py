"""
Tests for the DriverInputs domain model.
"""

from dataclasses import FrozenInstanceError

import pytest

from nordschleifen_coach.domain.telemetry.driver_inputs import DriverInputs


def test_driver_inputs_creation() -> None:
    """
    Verify that DriverInputs stores all driver control inputs correctly.
    """

    inputs = DriverInputs(
        throttle=0.75,
        brake=0.10,
        steering=-0.25,
        clutch=0.0,
        gear=3,
    )

    assert inputs.throttle == 0.75
    assert inputs.brake == 0.10
    assert inputs.steering == -0.25
    assert inputs.clutch == 0.0
    assert inputs.gear == 3


def test_driver_inputs_is_immutable() -> None:
    """
    Verify that DriverInputs instances are immutable.
    """

    inputs = DriverInputs(
        throttle=0.5,
        brake=0.0,
        steering=0.0,
        clutch=0.0,
        gear=2,
    )

    with pytest.raises(FrozenInstanceError):
        inputs.gear = 4
