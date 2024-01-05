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
        '|': (dirs['N'], dirs['S']), 
        '-': (dirs['E'], dirs['W']), 
        'L': (dirs['N'], dirs['E']), 
        'J': (dirs['N'], dirs['W']), 
        '7': (dirs['S'], dirs['W']), 
        'F': (dirs['E'], dirs['S']) 
        }

for k,v in dirs.items():
    new = np.add(start, v)
    if dirs[opp[k]] in moves[lines[new[0]][new[1]]]:
        print(f'Checked start direction {k} and found {moves[lines[new[0]][new[1]]]}')
        s_moves.append(k)
    else:
        print(f'Checked start direction {k} and didnt find {moves[lines[new[0]][new[1]]]}')
print(f'Start moves: {s_moves}')

moves['S'] = (dirs[s_moves[0]], dirs[s_moves[1]]) 
print(moves)

r_max = len(lines)
c_max = len(lines[0])


curr = tuple(np.add(start, dirs['S'][0]))
moves = 1
prev_move = ''

print(f'Curr = {curr}')
print(lines[1][1])
poss = tuple(np.add(curr, moves[lines[curr[0]][curr[1]]]))
print(f'Possibles: {poss}')


















