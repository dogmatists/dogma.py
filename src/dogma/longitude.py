# This is free and unencumbered software released into the public domain.

# See: https://dogma.dev/Longitude/
class Longitude:
    """A longitude."""

    radians: float

    def __init__(self, radians: float) -> None:
        self.radians = radians
