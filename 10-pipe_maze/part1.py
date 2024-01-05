import numpy as np

lines = [x for x in open('example.txt').read().split()]



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

s_moves = list()


moves = {
        '|': ('N', 'S'), 
        '-': ('E', 'W'), 
        'L': ('N', 'E'), 
        'J': ('N', 'W'), 
        '7': ('S', 'W'), 
        'F': ('E', 'S') 
        }

# Find the start position move options
for k,v in dirs.items():
    new = np.add(start, v)
    if opp[k] in moves[lines[new[0]][new[1]]]:
        print(f'Checked start direction {k} and found {moves[lines[new[0]][new[1]]]}')
        s_moves.append(k)
    else:
        print(f'Checked start direction {k} and didnt find {moves[lines[new[0]][new[1]]]}')
print(f'Start moves: {s_moves}')

moves['S'] = (s_moves[0], s_moves[1]) 
print(moves)

r_max = len(lines)
c_max = len(lines[0])


curr = start
move_count = 0
prev_move = ''

def makemove(curr, prev_move):
    pass

print(f'Curr = {curr}')

# While not at start with moves > 0
#   Get possible moves: if one == opp(prev) then do other, else do first
#   Increment counter

#while curr != start and move_count != 0:
next_move = lines[curr[0]][curr[1]]
if next_move != 'S':
    print(f'next move {moves[next_move]}')
    movement = [d for d in moves[next_move] if d != opp[prev_move]]
else:
    print(f'next move {s_moves[0]}')
    movement = moves['S'][0]

print('found movement: {movement}')

    






