from dataclasses import dataclass

from src.nordschleifen_coach.domain.value_objects.lap_time import LapTime


@dataclass(frozen=True, slots=True)
class Lap:
    """Represents a completed lap."""

    number: int
    lap_time: LapTime
    is_valid: bool

    def __post_init__(self) -> None:
        if self.number < 1:
            raise ValueError("Lap number must be at least 1.")
