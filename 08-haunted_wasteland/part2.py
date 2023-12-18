import re
from itertools import cycle

lines = [x for x in open('example3.txt').read().split('\n')]

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
position_check = False

while position_check == False:
    position_check = True
    for position in positions:
        position = nodes[position][0] if next(instructions_cycle) == 'L' else nodes[position][1]
        if position[2] != 'Z':
            position_check = False
    moves += 1
print(f'Total moves: {moves}')