from base.fraction import fractionBase
from debug import out

class Player:
    def __init__(self, name:str, fraction:fractionBase=None, fleets:list=[]) -> None:
        self.name = name
        self.fraction = fraction
        self.fleets = fleets
    
    def __repr__(self) -> str:
        return out('Player',{
            'name': self.name,
            'fraction': self.fraction,
            'fleets': self.fleets,
        })