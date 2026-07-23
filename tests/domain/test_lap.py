import pytest

from domain.entities.lap import Lap
from domain.value_objects.lap_time import LapTime


def test_create_lap() -> None:
    lap = Lap(
        number=1,
        lap_time=LapTime(523_481),
        is_valid=True,
    )

    assert lap.number == 1
    assert lap.lap_time.milliseconds == 523_481
    assert lap.is_valid is True


def test_lap_number_must_be_positive() -> None:
    with pytest.raises(ValueError):
        Lap(
            number=0,
            lap_time=LapTime(523_481),
            is_valid=True,
        )