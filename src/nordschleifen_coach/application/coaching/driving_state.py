from enum import Enum


class DrivingState(Enum):
    UNKNOWN = "unknown"

    IDLE = "idle"
    ACCELERATING = "accelerating"
    BRAKING = "braking"
    COASTING = "coasting"
    CORNERING = "cornering"