import pytest

from domain.value_objects.distance import Distance


def test_create_valid_distance() -> None:
    distance = Distance(meters=25_378.0)

    assert distance.meters == 25_378.0


def test_distance_cannot_be_negative() -> None:
    with pytest.raises(ValueError):
        Distance(meters=-1.0)