import numpy as np


ref = {
        'A': ((-1, -1), (3, 4)),
        'B': ((1, 2), (5, 5))
        }

s = (1,1)

directions = {
        'N': (-1, 0),
        'E': (0, 1),
        'S': (1, 0),
        'W': (0, -1)
        }

moves = {
        1: (directions['N'], directions['E']),
        2: (directions['W'], directions['E'])
        }


print(moves)
