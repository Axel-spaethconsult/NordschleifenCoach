"""
Parser for ACC wheel data.
"""

from nordschleifen_coach.infrastructure.acc.dto.acc_wheel_dto import (
    AccWheelDto,
)
from nordschleifen_coach.infrastructure.acc.dto.acc_wheel_state_dto import (
    AccWheelStateDto,
)


class WheelParser:
    """
    Parses wheel data from ACC physics.
    """

    def parse(self, physics) -> AccWheelStateDto:
        return AccWheelStateDto(
            front_left=self._create_wheel(
                physics,
                "front_left",
            ),
            front_right=self._create_wheel(
                physics,
                "front_right",
            ),
            rear_left=self._create_wheel(
                physics,
                "rear_left",
            ),
            rear_right=self._create_wheel(
                physics,
                "rear_right",
            ),
        )

    def _create_wheel(
        self,
        physics,
        wheel: str,
    ) -> AccWheelDto:
        return AccWheelDto(
            tyre_core_temperature=getattr(
                physics.tyre_core_temp,
                wheel,
            ),
            tyre_pressure=getattr(
                physics.wheel_pressure,
                wheel,
            ),
            brake_temperature=getattr(
                physics.brake_temp,
                wheel,
            ),
            brake_pressure=getattr(
                physics.brake_pressure,
                wheel,
            ),
            slip_ratio=getattr(
                physics.slip_ratio,
                wheel,
            ),
            slip_angle=getattr(
                physics.slip_angle,
                wheel,
            ),
            wheel_slip=getattr(
                physics.wheel_slip,
                wheel,
            ),
        )