import re
from itertools import cycle

lines = [x for x in open('input.txt').read().split('\n')]

instructions = lines[0]
instructions_cycle = cycle(instructions)
nodes = dict()

for l in lines[2:]:
    a,b,c = re.findall(r'[A-Z]{3}', l)
    nodes[a] = (b, c)

position = 'AAA'
moves = 0
while position != 'ZZZ':
    position = nodes[position][0] if next(instructions_cycle) == 'L' else nodes[position][1]
    moves += 1


print(f'Total moves: {moves}')