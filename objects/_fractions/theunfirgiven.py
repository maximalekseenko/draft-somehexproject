# imports
## base
from base.fraction import FractionBase
from base.unit import UnitBase, UNITTAG
from base.weapon import WeaponBase, WeaponNone, WEAPONTAG, WeaponSelector



# weapons
class WeaponMacrocannonsBattery(WeaponBase):
    name = 'Macrocannons Battery'
    tags = [
        WEAPONTAG.ARC_ABEAM,
        WEAPONTAG.HEAVY,
    ]
class WeaponPlasmaMacrocannonsBattery(WeaponBase):
    name = 'Plasma Macrocannons Battery'
    tags = [
        WEAPONTAG.ARC_ABEAM,
        WEAPONTAG.HEAVY,
        WEAPONTAG.PLASMA,
    ]
class WeaponTorpedos(WeaponBase):
    name = 'Torpedos'
    tags = [
        WEAPONTAG.ARC_PROW,
        WEAPONTAG.TORPEDO,
    ]
class WeaponLaunchBays(WeaponBase):
    name = 'Launch Bays'
    tags = [
        WEAPONTAG.ARC_PROW,
        WEAPONTAG.HANGAR,
    ]
class WeaponCannons(WeaponBase):
    name = 'Cannons'
    tags = [
        WEAPONTAG.ARC_DORSAL,
    ]
class WeaponBombardmentCannons(WeaponBase):
    name = 'Bombardment Cannons'
    tags = [
        WEAPONTAG.ARC_DORSAL,
        WEAPONTAG.MELTA,
    ]



# units
class UnitBattlebarge(UnitBase):
    name = 'Battlebarge'
    weapons = [
        WeaponSelector([
            WeaponNone,
            WeaponMacrocannonsBattery,
            WeaponPlasmaMacrocannonsBattery,
        ]),
        WeaponSelector([
            WeaponNone,
            WeaponMacrocannonsBattery,
            WeaponPlasmaMacrocannonsBattery,
        ]),
        WeaponSelector([
            WeaponNone,
            WeaponMacrocannonsBattery,
            WeaponPlasmaMacrocannonsBattery,
        ]),
        WeaponSelector([
            WeaponNone,
            WeaponMacrocannonsBattery,
            WeaponPlasmaMacrocannonsBattery,
        ]),
        WeaponSelector([
            WeaponNone,
            WeaponTorpedos,
            WeaponLaunchBays,
        ]),
        WeaponSelector([
            WeaponNone,
            WeaponTorpedos,
            WeaponLaunchBays,
        ]),
        WeaponSelector([
            WeaponNone,
            WeaponBombardmentCannons,
        ]),
    ]
    tags = [
        UNITTAG.SHIP,
        UNITTAG.SHIP_BATTLESHIP,
    ]



class UnitCruiser(UnitBase):
    name = 'Cruiser'
    weapons = [
        WeaponSelector([
            WeaponNone,
            WeaponMacrocannonsBattery,
            WeaponPlasmaMacrocannonsBattery,
        ]),
        WeaponSelector([
            WeaponNone,
            WeaponMacrocannonsBattery,
            WeaponPlasmaMacrocannonsBattery,
        ]),
        WeaponSelector([
            WeaponNone,
            WeaponTorpedos,
            WeaponLaunchBays,
        ]),
        WeaponSelector([
            WeaponNone,
            WeaponBombardmentCannons,
        ]),
    ]
    tags = [
        UNITTAG.SHIP,
        UNITTAG.SHIP_CRUISER,
    ]



class UnitHunter(UnitBase):
    name = 'Hunter Class Destroyer'
    weapons = [
        WeaponSelector([
            WeaponNone,
            WeaponTorpedos,
        ]),
        WeaponSelector([
            WeaponNone,
            WeaponCannons,
            WeaponBombardmentCannons,
        ]),
    ]
    tags = [
        UNITTAG.SHIP,
        UNITTAG.SHIP_ESCORT,
    ]



class UnitThunderhawk(UnitBase):
    name = 'Thunderhawk Gunships'
    weapons = []
    tags = [
        UNITTAG.SHIP,
        UNITTAG.SHIP_ATTACKCRAFT,
    ]



# fraction
class FractionTheUnforgiven(FractionBase):
    name = 'The Unforgiven'
    units = [
        UnitBattlebarge,
        UnitCruiser,
        UnitHunter,
        UnitThunderhawk,
    ]
    match_units = [
        UnitCruiser,
        UnitCruiser,
        UnitHunter,
        UnitHunter,
        UnitHunter,
    ]