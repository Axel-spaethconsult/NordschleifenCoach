"""
Data transfer object representing all wheel states read from
Assetto Corsa Competizione shared memory.
"""

from dataclasses import dataclass

from nordschleifen_coach.infrastructure.acc.dto.acc_wheel_dto import AccWheelDto


@dataclass(frozen=True, slots=True)
class AccWheelStateDto:
    """
    Raw wheel state values from ACC.
    """

    front_left: AccWheelDto
    front_right: AccWheelDto
    rear_left: AccWheelDto
    rear_right: AccWheelDto