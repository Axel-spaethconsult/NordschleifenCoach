from domain.entities.track import Track
from domain.value_objects.distance import Distance
from domain.value_objects.track_configuration import TrackConfiguration


def test_track_creation() -> None:
    track = Track(
        name="Nürburgring",
        configuration=TrackConfiguration.ENDURANCE_24H,

        country="Germany",
        length=Distance(25_378.0),
    )

    assert track.length.meters == 25_378.0