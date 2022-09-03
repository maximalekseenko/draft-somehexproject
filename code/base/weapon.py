from enum import Enum
from debug import class_info

class WEAPONTAG(Enum):
    NO_TAG=-1
    # arcs
    ARC_PROW = 1
    ARC_ABEAM = 2
    ARC_DORSAL = 3
    # ship type
    TURRET = 5
    HANGAR = 6
    TORPEDO = 8
    LIGHT = 9
    HEAVY = 9
    # type of ammo
    PLASMA = 10
    MELTA = 11
    FLAME = 12
    


class WeaponSelector:
    def set(self, index):
        self.weapon = self.weapons[index]()

    def __init__(self, weapons:list) -> None:
        if not weapons: weapons = [WeaponNone]
        self.weapons = weapons
        self.weapon = weapons[0]()

    

    def __repr__(self) -> str:
        return class_info('WeaponSelector',{
            'weapons:':self.weapons,
            'weapon': self.weapon,
        })



class WeaponBase:
    '''
    Base for a weapon

    ---
    setup next variables:
    * name
    * tags
    '''
    name = ''
    tags = []

    def __repr__(self) -> str:
        return class_info(
            self.name,
            {
                'tags':self.tags
            }) 



class WeaponNone(WeaponBase):
    name = 'noname'
    tags = [WEAPONTAG.NO_TAG]