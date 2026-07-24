"""
Maps ACC session state DTOs to domain models.
"""

from nordschleifen_coach.domain.telemetry.session_state import SessionState
from nordschleifen_coach.infrastructure.acc.dto.acc_session_state_dto import (
    AccSessionStateDto,
)


class SessionStateMapper:
    """
    Maps session state DTOs to domain models.
    """

    def map(self, dto: AccSessionStateDto) -> SessionState:
        """
        Maps a session state DTO to a domain model.
        """

        return SessionState(
            lap_number=dto.lap_number,
            lap_time=dto.lap_time,
            best_lap_time=dto.best_lap_time,
            is_valid_lap=dto.is_valid_lap,
            normalized_position=dto.normalized_position,
            distance_travelled=dto.distance_travelled,
        )