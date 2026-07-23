import pytest

from nordschleifen_coach.domain.value_objects.lap_time import LapTime


def test_create_valid_lap_time() -> None:
    lap_time = LapTime(milliseconds=523_481)

    assert lap_time.milliseconds == 523_481


def test_lap_time_must_be_positive() -> None:
    with pytest.raises(ValueError):
        LapTime(milliseconds=0)
