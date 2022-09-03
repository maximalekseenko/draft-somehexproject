from random import random
# base
from base.sector import SectorBase
# api


# classes
class RandomSector(SectorBase):
    PLANETS = [" ","░","▒","▓","█"]
    MAX_PLANETS = 5
    DIFFICULTY = 5
    MAX_PLANETS_PECENT = 0.15
    MIN_PLANETS_PECENT = 0.1

    def __init__(self, size: int) -> None:
        super().__init__(size, seed=int(random()*1000))
