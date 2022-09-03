# def perlin_noise(x, y, z):
#     X = int(x) & 255                  # FIND UNIT CUBE THAT
#     Y = int(y) & 255                  # CONTAINS POINT.
#     Z = int(z) & 255
#     x -= int(x)                                # FIND RELATIVE X,Y,Z
#     y -= int(y)                                # OF POINT IN CUBE.
#     z -= int(z)
#     u = fade(x)                                # COMPUTE FADE CURVES
#     v = fade(y)                                # FOR EACH OF X,Y,Z.
#     w = fade(z)
#     A = p[X  ]+Y; AA = p[A]+Z; AB = p[A+1]+Z      # HASH COORDINATES OF
#     B = p[X+1]+Y; BA = p[B]+Z; BB = p[B+1]+Z      # THE 8 CUBE CORNERS,
 
#     return lerp(w, lerp(v, lerp(u, grad(p[AA  ], x  , y  , z   ),  # AND ADD
#                                    grad(p[BA  ], x-1, y  , z   )), # BLENDED
#                            lerp(u, grad(p[AB  ], x  , y-1, z   ),  # RESULTS
#                                    grad(p[BB  ], x-1, y-1, z   ))),# FROM  8
#                    lerp(v, lerp(u, grad(p[AA+1], x  , y  , z-1 ),  # CORNERS
#                                    grad(p[BA+1], x-1, y  , z-1 )), # OF CUBE
#                            lerp(u, grad(p[AB+1], x  , y-1, z-1 ),
#                                    grad(p[BB+1], x-1, y-1, z-1 ))))
 
# def fade(t): 
#     return t ** 3 * (t * (t * 6 - 15) + 10)
 
# def lerp(t, a, b):
#     return a + t * (b - a)
 
# def grad(hash, x, y, z):
#     h = hash & 15                      # CONVERT LO 4 BITS OF HASH CODE
#     u = x if h<8 else y                # INTO 12 GRADIENT DIRECTIONS.
#     v = y if h<4 else (x if h in (12, 14) else z)
#     return (u if (h&1) == 0 else -u) + (v if (h&2) == 0 else -v)
 
# p = [None] * 512
# permutation = [151,160,137,91,90,15,
#    131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,
#    190, 6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,
#    88,237,149,56,87,174,20,125,136,171,168, 68,175,74,165,71,134,139,48,27,166,
#    77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,
#    102,143,54, 65,25,63,161, 1,216,80,73,209,76,132,187,208, 89,18,169,200,196,
#    135,130,116,188,159,86,164,100,109,198,173,186, 3,64,52,217,226,250,124,123,
#    5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,
#    223,183,170,213,119,248,152, 2,44,154,163, 70,221,153,101,155,167, 43,172,9,
#    129,22,39,253, 19,98,108,110,79,113,224,232,178,185, 112,104,218,246,97,228,
#    251,34,242,193,238,210,144,12,191,179,162,241, 81,51,145,235,249,14,239,107,
#    49,192,214, 31,181,199,106,157,184, 84,204,176,115,121,50,45,127, 4,150,254,
#    138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180]
# for i in range(256):
#     p[256+i] = p[i] = permutation[i]


def perlin_noise(*point):
    unit_cube = [int(axis) & 255 for axis in point]
    relative_cube = [axis-int(axis) for axis in point]
    fade_curves  = [fade(i) for i in relative_cube]
    A = p[unit_cube[0]  ]+unit_cube[1]; AA = p[A]+unit_cube[2]; AB = p[A+1]+unit_cube[2]      # HASH COORDINATES OF
    B = p[unit_cube[0]+1]+unit_cube[1]; BA = p[B]+unit_cube[2]; BB = p[B+1]+unit_cube[2]      # THE 8 CUBE CORNERS,

    ##### A
    hash = list()
    n = len(point)
    coords = [1] * n
    def f(axis):
        coords[axis] = coords[axis]+1 & 1
        if axis != 0:
            return lerp(fade_curves[n-axis], f(axis-1), f(axis-1))

        t = 0
        for i in range(n):
            t = p[t + unit_cube[i] + coords[i]]
        ORIG =[
        [p[AA  ],relative_cube[0]  , relative_cube[1]  , relative_cube[2]  ],
        [p[BA  ],relative_cube[0]-1, relative_cube[1]  , relative_cube[2]  ],
        [p[AB  ],relative_cube[0]  , relative_cube[1]-1, relative_cube[2]  ],
        [p[BB  ],relative_cube[0]-1, relative_cube[1]-1, relative_cube[2]  ],
        [p[AA+1],relative_cube[0]  , relative_cube[1]  , relative_cube[2]-1],
        [p[BA+1],relative_cube[0]-1, relative_cube[1]  , relative_cube[2]-1],
        [p[AB+1],relative_cube[0]  , relative_cube[1]-1, relative_cube[2]-1],
        [p[BB+1],relative_cube[0]-1, relative_cube[1]-1, relative_cube[2]-1]]
        GRAD = list(map(lambda x:grad(*x),ORIG))
        A = [t]+[relative_cube[i]-coords[i] for i in range(n)]
        print(ORIG.index(A))
        # for i in GRAD:
        #     print(GRAD.count(i))
        # print([
        # [p[AA  ],relative_cube[0]  , relative_cube[1]  , relative_cube[2]  ],
        # [p[BA  ],relative_cube[0]-1, relative_cube[1]  , relative_cube[2]  ],
        # [p[AB  ],relative_cube[0]  , relative_cube[1]-1, relative_cube[2]  ],
        # [p[BB  ],relative_cube[0]-1, relative_cube[1]-1, relative_cube[2]  ],
        # [p[AA+1],relative_cube[0]  , relative_cube[1]  , relative_cube[2]-1],
        # [p[BA+1],relative_cube[0]-1, relative_cube[1]  , relative_cube[2]-1],
        # [p[AB+1],relative_cube[0]  , relative_cube[1]-1, relative_cube[2]-1],
        # [p[BB+1],relative_cube[0]-1, relative_cube[1]-1, relative_cube[2]-1]
        # ].index(
        #     [t]+[relative_cube[i]-coords[i] for i in range(n)]
        #     ))

        return grad(t, * [relative_cube[i]-coords[i] for i in range(n)])
    return lerp(fade_curves[n-1], f(n-1), f(n-1))

###### B
    return lerp(fade_curves[2], 
        lerp(fade_curves[1], 
            lerp(fade_curves[0], 
                grad(p[AA  ], relative_cube[0]  , relative_cube[1]  , relative_cube[2]   ),  # AND ADD
                grad(p[BA  ], relative_cube[0]-1, relative_cube[1]  , relative_cube[2]   )), # BLENDED
            lerp(fade_curves[0], 
                grad(p[AB  ], relative_cube[0]  , relative_cube[1]-1, relative_cube[2]   ),  # RESULTS
                grad(p[BB  ], relative_cube[0]-1, relative_cube[1]-1, relative_cube[2]   ))),# FROM  8
        lerp(fade_curves[1], 
            lerp(fade_curves[0], 
                grad(p[AA+1], relative_cube[0]  , relative_cube[1]  , relative_cube[2]-1 ),  # CORNERS
                grad(p[BA+1], relative_cube[0]-1, relative_cube[1]  , relative_cube[2]-1 )), # OF CUBE
            lerp(fade_curves[0], 
                grad(p[AB+1], relative_cube[0]  , relative_cube[1]-1, relative_cube[2]-1 ),
                grad(p[BB+1], relative_cube[0]-1, relative_cube[1]-1, relative_cube[2]-1 ))))

 
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
