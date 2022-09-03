# api
from api.HAPI import HexField, Hex

class SectorHex(Hex):
    value = 0

# class
class SectorBase(HexField):
    '''
    Base for a sector

    ---
    setup next variables:
    * name
    * size
    '''

    name = ''
    hexType = SectorHex



