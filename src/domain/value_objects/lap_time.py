from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class LapTime:
    """Represents a lap time in milliseconds."""

    milliseconds: int

    def __post_init__(self) -> None:
        if self.milliseconds <= 0:
            raise ValueError("Lap time must be greater than zero.")