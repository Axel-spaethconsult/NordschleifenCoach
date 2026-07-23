from enum import Enum


class TrackConfiguration(str, Enum):
    """Represents a track configuration."""

    GP = "GP"
    ENDURANCE_24H = "24h"