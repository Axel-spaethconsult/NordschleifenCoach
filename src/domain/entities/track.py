from dataclasses import dataclass

from domain.value_objects.distance import Distance
from domain.value_objects.track_configuration import TrackConfiguration


@dataclass(frozen=True, slots=True)
class Track:
    """Represents a racing track."""

    name: str
    configuration: TrackConfiguration
    country: str
    length: Distance