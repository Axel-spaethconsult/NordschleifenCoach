from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Track:
    """Represents a racing track."""

    name: str
    configuration: str
    country: str
    length_m: float
    