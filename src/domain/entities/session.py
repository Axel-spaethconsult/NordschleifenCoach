from dataclasses import dataclass

from domain.entities.lap import Lap


@dataclass(frozen=True, slots=True)
class Session:
    """Represents a driving session."""

    laps: tuple[Lap, ...]
    