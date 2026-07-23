from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Distance:
    """Represents a distance in meters."""

    meters: float

    def __post_init__(self) -> None:
        if self.meters < 0:
            raise ValueError("Distance cannot be negative.")
