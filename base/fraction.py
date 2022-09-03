from debug import class_info



class FractionBase:
    '''
    Base for a fraction

    ---
    setup next variables:
    * name
    * units
    * match_units
    '''

    name = ''
    units = []
    match_units = []


    def get_match_units(self) -> list: 
        return [unit() for unit in self.match_units]
    '''function to get match starting units'''


    def __repr__(self) -> str:
        return class_info(self.name, {
            'units': self.units,
            'match units': self.match_units,
            }
        )