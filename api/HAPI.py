from typing import Union


class Position:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x}, {self.y}]"
    
    def __getitem__(self, key):
        if key < 0 or key > 1: raise IndexError(f'Position has only 2 axes ({key} requested)')
        if key == 0: return self.x
        if key == 1: return self.y

    def __setitem__(self, key, value):
        if key < 0 or key > 1: raise IndexError(f'Position has only 2 axes ({key} requested)')
        if value.__class__ != int: raise TypeError(f'Position axis value can only be int ({value.__class__} given)')
        if key == 0: self.x = value; return
        if key == 1: self.y = value; return

    def __add__(self, other):
        if other.__class__ != list and other.__class__ != self.__class__: raise TypeError(f'can only add list of Position (not "{other.__class__}") to Position')
        if other.__class__ == list and len(other) != 2: raise TypeError(f'can only add list with length of 2 (not {len(other)}) to Position')
        return Position(self[0] + other[0], self[1] + other[1])

    def __sub__(self, other):
        if other.__class__ != list and other.__class__ != self.__class__: raise TypeError(f'can only add list of Position (not "{other.__class__}") to Position')
        if other.__class__ == list and len(other) != 2: raise TypeError(f'can only add list with length of 2 (not {len(other)}) to Position')
        return Position(self[0] - other[0], self[1] - other[1])

    def __mul__(self, other):
        if other.__class__ != int: raise TypeError(f'can only multiply int (not "{other.__class__}") with Position')
        return Position(self[0] * other, self[1] * other)

    def __iter__(self):
        return iter((self.x, self.y))

    def __eq__(self, other):
        if other.__class__ != list and other.__class__ != self.__class__: raise TypeError(f'can only compair list of Position (not "{other.__class__}") with Position')
        if other.__class__ == list and len(other) != 2: raise TypeError(f'can only compair list with length of 2 (not {len(other)}) with Position')
        return self[0] == other[0] and self[1] == other[1]

    def __bool__(self):
        return self[0] != 0 or self[1] != 0

    def __neg__(self):
        return Position(-self[0], -self[1])


# constants
AXES = {
    'x':Position(1,0),
    'y':Position(1,1),
    'z':Position(0,1)}



# classes
class Hex:
    ''''''
    @property
    def position(self) -> Position: return self._position

    value = None

    def __init__(self, position) -> None:
        self._position = Position(*position)

    def __str__(self):
        return str(self.value)

    def gen(self, gen_value:int):
        self.gen_value = gen_value



class HexField:
    '''Base for creating custom hex field'''

    # attributes
    @property
    def size(self) -> int: return self._size
    '''length of the field diagonal. MUST be odd'''

    @property
    def hexType(self) -> type: return self._hexType
    '''type of point on field'''

    @property
    def field(self) -> type: return self._field
    '''type of point on field'''

    @property
    def center(self) -> type: return [self.size//2]*2
    '''type of point on field'''


    # inits
    def __init__(self, size:int, hexType:type, **kargs) -> None:
        '''args:
        * size - length of the field diagonal. MUST be odd.
        * hexType - type of point on field.

        kargs:
        * separator - repr values separation char
        * bounds - repr line's first and last chars list
        * offfield - repr values off field char
        '''
        # variables
        ## size
        self._size = size
        if self.size % 2 == 0: raise
        ## hexType
        self._hexType = hexType
        if self.hexType == None: raise
        ## field
        self.setup_field()
        ## repr
        
        self.setup_repr(**{key: value for key, value in kargs.items() if key in ["separator", "bounds", "offfield"]})


    def setup_field(self) -> None:
        '''resets field matrix'''
        self._field = [[(
                    self.hexType([_x,_y]) 
                    if self.is_on_field(_x, _y) 
                    else None)
                for _y in range(self.size)]
            for _x in range(self.size)]


    def setup_repr(self, separator='|', bounds=['[',']'], offfield='') -> None:
        self.repr_separator=separator
        self.repr_bounds=bounds
        self.repr_offfield=offfield


    # basic
    def __repr__(self) -> str:
        max_value = max(map(lambda hex:len(str(hex)),[self.repr_offfield]+self.get_all_hexes()))

        return '\n'.join([f"{self.repr_bounds[0]}{f'{self.repr_separator}'.join([(str(self.field[x][y]) if self.is_on_field(x,y) else self.repr_offfield).ljust(max_value) for x in range(len(self))])}{self.repr_bounds[1]}" for y in range(len(self))])
    
    def __len__(self) -> int:
        return self.size


    # # gen
    # def gen(self, frec:int=None, seed:int=0):
    #     '''generates random values for each hex on field'''
    #     if frec == None: frec = self.size+1
        
    #     for coords in self.get_all_coords():
    #         self.__getitem__(*coords).gen(pnoise2((coords[0]+1)/frec,(coords[1]+1)/frec,base=seed))


    # item
    def __getitem__(self, position:Union[Position, list]) -> Hex:
        if not self.is_on_field(position): raise IndexError
        return self.field[position[0]][position[1]]
   

    # @coords_as_sep(1)
    # def __setitem__(self, x:int, y:int, value:Hex) -> None:
    #     raise
    #     if not self.is_on_field(x,y): raise IndexError
    #     if type(value) != Hex: raise TypeError
    #     self.field[x][y] = value
        

    def is_on_field(self, x:int, y:int) -> bool:
        '''checks if point[x, y] is on field'''
        if self.size + x - y <= self.size // 2: return False
        if self.size - x + y <= self.size // 2: return False
        if x < 0 or x >= self.size: return False
        if y < 0 or y >= self.size: return False
        return True
    
    def is_point_on_field(self, position:Union[Position, list]) -> bool:
        '''checks if point is on field'''
        return self.is_on_field(*position)
           


    # geometric gets
    def get_vector(x:int=0, y:int=0, z:int=0) -> Position:
        new_vector = Position(0,0)
        if x != 0: new_vector += AXES['x'] * x
        if y != 0: new_vector += AXES['y'] * y
        if z != 0: new_vector += AXES['z'] * z
        return new_vector
        
        
    def get_move(self, from_position:list, vactor:list) -> list:
        '''returns a new position, witch was burned'''
        new_position = list(from_position)
        new_position[0] += 1
        new_position[1] += 1
        return new_position


    def get_line_from(self, from_position:list, directions:dict) -> list:
        return_position = list(from_position)
        # get
        for axis in axes.items():
            for i in range(2): return_position[i]+=AXES[axis[0]][i]*axis[1]
        # validate
        if not self.is_on_field(return_position): return None
        # return
        return return_position
        


    def get_line_between(self, start_position:list, end_position) -> list:
        return_positions = []
        cur_position = list(start_position)
        
        # step_x, step_y, step_z = 0
        # for i in range(max_range):
        #     self.get_move(cur_position,
        #         {'x':1},{'y':1},{'z':1}
        #         )
        #     return_positions
        # return return_position
    


    # getters
    def get_center_hex(self) -> list:
        return self.field[self.size//2, self.size//2]

    def get_center_coord(self) -> list:
        return [self.size//2, self.size//2]

    def get_all_hexes(self) -> list:
        ret = []
        for x in range(self.size):
            for y in range(self.size):
                if self.is_on_field(x,y):
                    ret.append(self.field[x][y])
        return ret
        
    def get_all_coords(self) -> list:
        ret = []
        for x in range(self.size):
            for y in range(self.size):
                if self.is_on_field(x,y):
                    ret.append([x,y])
        return ret
    
    def get_hex_neighbours(x:int, y:int, z:int) -> list:
        return [
            [x+1,y+1], [x+0,y+1],
            [x+1,y+0], [x-1,y+0],
            [x+0,y-1], [x-1,y-1]]