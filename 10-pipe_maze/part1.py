import numpy as np

lines = [x for x in open('input.txt').read().split()]



#    | is a vertical pipe connecting north and south.
#    - is a horizontal pipe connecting east and west.
#    L is a 90-degree bend connecting north and east.
#    J is a 90-degree bend connecting north and west.
#    7 is a 90-degree bend connecting south and west.
#    F is a 90-degree bend connecting south and east.
#    . is ground; there is no pipe in this tile.
#    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
#

# Find start position
for r, line in enumerate(lines):
    if 'S' in line:
        start = (r, line.index('S'))

# Set up dictionaries for movements and the reverse movements
dirs = {
        'N': (-1, 0),
        'E': (0, 1),
        'S': (1, 0),
        'W': (0, -1)
        }

opp = {
        'N': 'S',
        'S': 'N',
        'E': 'W',
        'W': 'E'
        }


moves = {
        '|': ('N', 'S'), 
        '-': ('E', 'W'), 
        'L': ('N', 'E'), 
        'J': ('N', 'W'), 
        '7': ('S', 'W'), 
        'F': ('E', 'S'),
        '.': ()
        }


# Find the start position move options
s_moves = list()

# Check each direction from S. If it contains a symbol which would allow movement back to S then this
# is a valid move from S. Record which of the 4 movements from S are valid.
for k,v in dirs.items():
    new = np.add(start, v)
    if opp[k] in moves[lines[new[0]][new[1]]]:
        s_moves.append(k)

moves['S'] = (s_moves[0], s_moves[1]) 

r_max = len(lines)
c_max = len(lines[0])

tupleadd = lambda x, y: tuple(np.add(x, y))

curr = start
move_count = 0
prev_move = ''



# While not at start with moves > 0
#   Get possible moves: if one == opp(prev) then do other, else do first
#   Increment counter

while not (curr == start and move_count > 0):
    next_move = lines[curr[0]][curr[1]]
    if next_move != 'S':
        movement = [d for d in moves[next_move] if d != opp[prev_move]][0]
        curr = tupleadd(curr, dirs[movement])
        prev_move = movement
    else:
        movement = moves['S'][0]
        curr = tupleadd(curr, dirs[movement])
        prev_move = movement

    move_count += 1

# The above for loop takes us all the way around the path. The furthest square is 1/2 total distance.
print(f'Total moves {move_count} so furthest distance is {int(move_count/2)}')





