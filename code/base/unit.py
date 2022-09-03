from enum import Enum
from base.weapon import WeaponSelector
from debug import class_info



class UNITTAG(Enum):
    NO_TAG=-1
    SHIP=0
    ## ship types
    SHIP_TORPEDO=1
    SHIP_BATTLESHIP=1
    SHIP_GRANDCRUISER=2
    SHIP_CRUISER=2
    SHIP_ESCORT=3
    SHIP_ATTACKCRAFT=3



class UnitBase:
    '''
    Base for a unit

    ---
    setup this variables:
    * name
    * weapons
    * tags
    '''

    name = ''
    weapons = [WeaponSelector([])]
    tags = [UNITTAG.NO_TAG]

    def __init__(self, weapons:list=[]) -> None:
        for i in range(len(weapons)):
            self.weapons[i].set(weapons[i])
        
    def __repr__(self) -> str:
        return class_info(self.name,
            {
                "weapons": self.weapons,
                'tags':self.tags
            }) 
