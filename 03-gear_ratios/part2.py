import re
import itertools

input = [x for x in open('input.txt').read().split('\n')]
punctpos = set()
all_surrounds = dict()
value_lookup = dict()
v = 0
total = 0


# Find all the *s
for rownum, row in enumerate(input):
    for colnum, char in enumerate(row):
        if char == '*':
            punctpos.add((rownum, colnum))


# For each number identify the coordinates surrounding
# We need to add on the diagonals and make sure the new coordinate actually exists
# The check if any of them are in punctpos - if they are then this is a valid part
# NOTE - used re.finditer to avoid edge case

linewidth = range(len(input[0]))
for rownum, row in enumerate(input):
    for n in re.finditer(r'\d+', row):
        value = int(n.group())
        span = n.span()
        surrounds = list()

        # left
        if span[0]-1 in linewidth:
            surrounds.append((rownum, span[0]-1))
        # right
        if span[0]+1 in linewidth:
            surrounds.append((rownum, span[1]))
        # top
        surrounds.extend([(rownum-1, x) for x in range(span[0]-1, span[1]+1) if rownum-1 >=0 and x in linewidth])
        # bottom
        surrounds.extend([(rownum+1, x) for x in range(span[0]-1, span[1]+1) if rownum+1 < len(input) and x in linewidth])

        # Now keep the ones which have contact with an asterisk
        for s in surrounds:
            if s in punctpos:
                all_surrounds[v] = surrounds
                value_lookup[v] = value
                v += 1
                break


v_length = len(value_lookup)
for p in punctpos:
    # combinations() returns an iterator so we need to create it each time
    combinations = itertools.combinations(range(v_length), 2)
    for i, j in combinations:
        if p in all_surrounds[i] and p in all_surrounds[j]:
            total += value_lookup[i] * value_lookup[j]

print(f'The final total is {total}')


