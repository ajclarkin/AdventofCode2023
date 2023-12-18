import re
from itertools import cycle
from math import lcm

lines = [x for x in open('input.txt').read().split('\n')]

instructions = lines[0]
instructions_cycle = cycle(instructions)
nodes = dict()

positions = list()
for l in lines[2:]:
    a,b,c = re.findall(r'[A-Z1-9]{3}', l)
    nodes[a] = (b, c)
    if a[2] == 'A':
        positions.append(a)


moves = 0
move_count = dict()
position_check = False

while position_check == False:
    position_check = True
    move = 0 if next(instructions_cycle) == 'L' else 1

    for key, position in enumerate(positions):
        positions[key] = nodes[position][move]
        if position[2] != 'Z':
            position_check = False
        else:
            if key not in move_count.keys():
                move_count[key] = moves
    if position_check == False: moves += 1

    if len(move_count.keys()) == len(positions):
        break

# Need to use a star to access the contents of the dict
print(lcm(*move_count.values()))