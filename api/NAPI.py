def perlin_noise(x,y,z) -> float:
    # FIND UNIT CUBE THAT CONTAINS POINT.
    unit_cube = [int(i) & 255 for i in point] # orig-X,Y,Z
    # FIND RELATIVE X,Y,Z OF POINT IN CUBE. (offset vector)
    relative_cube = [i-int(i) for i in point] # orig-x,y,z
    # COMPUTE FADE CURVES FOR EACH OF X,Y,Z.
    fade_curves  = [fade(i) for i in relative_cube] # orig-u,v,w
    # HASH COORDINATES OF THE 8 CUBE CORNERS,
    hash = list()
    n = len(point)
    coords = [1] * n
    
    def f(axis):
        coords[axis] = coords[axis]+1 & 1
        if axis != 0: 
            return lerp(fade_curves[n-axis],f(axis-1),f(axis-1))

        t = unit_cube[0] + coords[0]
        for i in range(1,n):
            t = p[t] + unit_cube[i] + coords[i]

        return grad(t, * [relative_cube[i]-coords[i] for i in range(n)])

    return lerp(fade_curves[n-1],f(n-1),f(n-1))

def fade(t): 
    return t ** 3 * (t * (t * 6 - 15) + 10)
 
def lerp(t, a, b):
    return a + t * (b - a)
 
def grad(hash, x, y, z):
    h = hash & 15                      # CONVERT LO 4 BITS OF HASH CODE
    u = x if h<8 else y                # INTO 12 GRADIENT DIRECTIONS.
    v = y if h<4 else (x if h in (12, 14) else z)
    return (u if (h&1) == 0 else -u) + (v if (h&2) == 0 else -v)

p = [None] * 512
permutation = [151,160,137,91,90,15,
   131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,
   190, 6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,
   88,237,149,56,87,174,20,125,136,171,168, 68,175,74,165,71,134,139,48,27,166,
   77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,
   102,143,54, 65,25,63,161, 1,216,80,73,209,76,132,187,208, 89,18,169,200,196,
   135,130,116,188,159,86,164,100,109,198,173,186, 3,64,52,217,226,250,124,123,
   5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,
   223,183,170,213,119,248,152, 2,44,154,163, 70,221,153,101,155,167, 43,172,9,
   129,22,39,253, 19,98,108,110,79,113,224,232,178,185, 112,104,218,246,97,228,
   251,34,242,193,238,210,144,12,191,179,162,241, 81,51,145,235,249,14,239,107,
   49,192,214, 31,181,199,106,157,184, 84,204,176,115,121,50,45,127, 4,150,254,
   138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180]
for i in range(256):
    p[256+i] = p[i] = permutation[i]
 





def gen3(x:int, y:int, z:int, maximum:int, minimum=0, step=1, reverse=False, seed:int=0, freq=10) -> int:

    # get noice 
    value = pnoise3(x/freq, y/freq, z/freq, base=seed)

    ## noice returns -1<value<1
    ## but we need minimum<=value<=maximum
    value = abs(value)
    value *= maximum - minimum + 1
    value += minimum

    # raise to integers 
    value = round(value-0.5)

    # return final value
    return value

