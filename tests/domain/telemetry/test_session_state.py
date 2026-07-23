"""
Tests for the SessionState domain model.
"""

from dataclasses import FrozenInstanceError

import pytest

from nordschleifen_coach.domain.telemetry.session_state import SessionState


def test_session_state_creation() -> None:
    """
    Verify that SessionState stores all session values correctly.
    """

    session = SessionState(
        lap_number=5,
        lap_time=93.527,
        best_lap_time=92.814,
        is_valid_lap=True,
        normalized_position=0.432,
        distance_travelled=10837.4,
    )

    assert session.lap_number == 5
    assert session.lap_time == 93.527
    assert session.best_lap_time == 92.814
    assert session.is_valid_lap is True
    assert session.normalized_position == 0.432
    assert session.distance_travelled == 10837.4


def test_session_state_is_immutable() -> None:
    """
    Verify that SessionState instances are immutable.
    """

    session = SessionState(
        lap_number=1,
        lap_time=0.0,
        best_lap_time=0.0,
        is_valid_lap=True,
        normalized_position=0.0,
        distance_travelled=0.0,
    )

    with pytest.raises(FrozenInstanceError):
        session.lap_number = 2
