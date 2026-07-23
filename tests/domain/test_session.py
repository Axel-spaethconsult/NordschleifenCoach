from nordschleifen_coach.domain.entities.lap import Lap
from nordschleifen_coach.domain.entities.session import Session
from nordschleifen_coach.domain.value_objects.lap_time import LapTime


def test_create_session() -> None:
    lap = Lap(
        number=1,
        lap_time=LapTime(523_481),
        is_valid=True,
    )

    session = Session(
        laps=(lap,),
    )

    assert len(session.laps) == 1
