from api.HAPI import Hex

class SHex(Hex):
    def __init__(self) -> None:
        super().__init__()

        self.fleets = []
        self.planets = []

    def __repr__(self):
        return str(self.planets)
    