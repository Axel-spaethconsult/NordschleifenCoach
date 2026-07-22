from domain.entities.track import Track


def test_track_creation():
    """A track can be created with valid data."""

    track = Track(
        name="Nürburgring",
        configuration="24h",
        country="Germany",
        length_m=25_378.0,
    )

    assert track.name == "Nürburgring"
    assert track.configuration == "24h"
    assert track.country == "Germany"
    assert track.length_m == 25_378.0