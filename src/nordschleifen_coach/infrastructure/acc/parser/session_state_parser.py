"""
Parser for ACC session state.
"""

from nordschleifen_coach.infrastructure.acc.dto.acc_session_state_dto import (
    AccSessionStateDto,
)


class SessionStateParser:
    """
    Parses session data from ACC graphics.
    """

    def parse(self, graphics) -> AccSessionStateDto:
        return AccSessionStateDto(
            lap_number=graphics.completed_lap,
            lap_time=graphics.current_time,
            best_lap_time=graphics.best_time,
            is_valid_lap=graphics.is_valid_lap,
            normalized_position=graphics.normalized_car_position,
            distance_travelled=graphics.distance_traveled,
        )