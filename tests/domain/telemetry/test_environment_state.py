"""
Tests for the EnvironmentState domain model.
"""

from dataclasses import FrozenInstanceError

import pytest

from nordschleifen_coach.domain.telemetry.environment_state import (
    EnvironmentState,
)


def test_environment_state_creation() -> None:
    """
    Verify that EnvironmentState stores all environmental values correctly.
    """

    environment = EnvironmentState(
        air_temperature=21.5,
        track_temperature=34.8,
        track_grip=0.98,
        rain_intensity=0.0,
    )

    assert environment.air_temperature == 21.5
    assert environment.track_temperature == 34.8
    assert environment.track_grip == 0.98
    assert environment.rain_intensity == 0.0


def test_environment_state_is_immutable() -> None:
    """
    Verify that EnvironmentState instances are immutable.
    """

    environment = EnvironmentState(
        air_temperature=20.0,
        track_temperature=30.0,
        track_grip=1.0,
        rain_intensity=0.0,
    )

    with pytest.raises(FrozenInstanceError):
        environment.air_temperature = 25.0
