from debug import out


class Fleet:
    def __init__(self, ships:list=[], auxillary:list=[]) -> None:
        self.ships = ships
        self.auxillary = auxillary
    
    def __repr__(self) -> str:
        return out('Fleet', {
            'ships':self.ships,
            'auxillary':self.auxillary
        })
#         return f'\
#  -Fleet \n\
#  ├ ships:{self.ships} \n\
#  └ auxillary:{self.auxillary}'